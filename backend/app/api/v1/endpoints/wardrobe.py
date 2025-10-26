import json
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
import google.generativeai as genai
from app.core.config import GEMINI_API_KEY
from app.core.db import supabase, get_current_user
from pydantic import BaseModel, Field # We'll use this for the AI response
import uuid

router = APIRouter()

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Set up the model for JSON output
generation_config = genai.GenerationConfig(
    response_mime_type="application/json",
)
vision_model = genai.GenerativeModel(
    'gemini-1.5-flash',
    generation_config=generation_config
)

# --- Define the Pydantic model for the AI's response ---
# This forces the AI to be structured
class AIClothingTags(BaseModel):
    description: str = Field(description="A brief 2-5 word description, e.g., 'Blue Ripped Jeans'")
    category: str = Field(description="e.g., top, bottom, shoes, outerwear, accessories")
    subcategory: str = Field(description="e.g., t-shirt, jeans, sneakers, blazer")
    colors: list[str] = Field(description="A list of 1-2 primary colors")
    pattern: str = Field(description="e.g., solid, striped, floral, plaid, graphic")
    style_tags: list[str] = Field(description="e.g., casual, formal, sporty, vintage, gen z")
    formality_level: int = Field(description="A single integer from 1 (very casual) to 5 (very formal)")

# --- This is your "Vision Tagger" Prompt ---
VISION_TAGGER_PROMPT = f"""
You are an expert fashion data tagger. Analyze this image of a clothing item.
You MUST return ONLY a single, valid JSON object (no other text) that
strictly follows this JSON Schema:

{AIClothingTags.model_json_schema()}
"""

@router.post("/add")
async def add_wardrobe_item(
    user = Depends(get_current_user),
    file: UploadFile = File(...)
):
    """
    Uploads a clothing item, analyzes it with AI, and adds it to the user's wardrobe.
    """
    try:
        user_id = user.id
        
        # Read the image file
        contents = await file.read()
        
        # --- 1. Upload to Supabase Storage ---
        # Create a unique file path
        file_extension = file.filename.split('.')[-1]
        file_path = f"{user_id}/{uuid.uuid4()}.{file_extension}"
        
        storage_response = supabase.storage.from_("wardrobe-images").upload(
            path=file_path,
            file=contents,
            file_options={"content-type": file.content_type}
        )
        
        # Get the public URL
        public_url_response = supabase.storage.from_("wardrobe-images").get_public_url(file_path)
        image_url = public_url_response

        # --- 2. Analyze with AI ---
        # Create the "prompt part" for the Vision model
        image_part = {
            "mime_type": file.content_type,
            "data": contents
        }
        
        # Call the AI
        response = vision_model.generate_content([VISION_TAGGER_PROMPT, image_part])
        
        # Parse the AI's JSON response
        ai_data = json.loads(response.text)
        
        # --- 3. Save to Database ---
        # Combine all data into one object
        item_to_save = {
            "owner_id": user_id,
            "image_url": image_url,
            **ai_data  # Unpack all the fields from the AI's response
        }
        
        # Insert into the 'wardrobe_items' table
        db_response = supabase.table("wardrobe_items").insert(item_to_save).execute()
        
        if not db_response.data:
            raise HTTPException(status_code=500, detail="Failed to save item to database.")

        # 4. Return the new item (as defined in API_CONTRACT.md)
        return db_response.data[0]

    except Exception as e:
        print(f"Error in /add: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/")
def get_wardrobe_items(user = Depends(get_current_user)):
    """
    Gets all wardrobe items for the logged-in user.
    """
    try:
        user_id = user.id
        data = supabase.table("wardrobe_items").select("*").eq("owner_id", user_id).order("created_at", desc=True).execute()
        return data.data
    except Exception as e:
        print(f"Error in /get: {e}")
        raise HTTPException(status_code=500, detail=str(e))