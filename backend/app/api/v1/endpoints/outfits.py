import json
from fastapi import APIRouter, Depends, HTTPException
import google.generativeai as genai
from app.core.config import GEMINI_API_KEY
from app.core.db import supabase, get_current_user # <-- IMPORT new stuff
from app.core.models import GenerateRequest, OutfitResponse # <-- IMPORT models
from supabase.lib.client_options import ClientOptions


router = APIRouter()

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)
# Set up the model to ONLY output JSON
generation_config = genai.GenerationConfig(
    response_mime_type="application/json",
)
model = genai.GenerativeModel(
    'gemini-1.5-flash',
    generation_config=generation_config
)

# This is your "Master Prompt"
OUTFIT_GENERATOR_PROMPT = """
You are "Stylo", an expert AI fashion stylist. You can seamlessly translate
between styles (like Gen X and Gen Z) and occasions.

A user needs an outfit. Their request is:
- Occasion: "{occasion}"
- Desired Style: "{style_vibe}"

Here is the user's *entire* available wardrobe, as a JSON list.
You must use *only* items from this list.
{wardrobe_json}

Your task:
1.  Generate 3 complete outfit combinations.
2.  Each outfit MUST be a list of `item_id`s from the wardrobe.
3.  For each outfit, provide a `why` explanation, describing how it fits the
    occasion and style.
4.  Return ONLY a valid JSON list (no other text) that follows this format:
    [
      {{
        "outfit_items": ["item_id_1", "item_id_2"],
        "explanation": "Why this works...",
        "tip": "A styling tip..."
      }}
    ]
"""

@router.post("/generate", response_model=OutfitResponse)
def generate_outfit(
    request: GenerateRequest,  # <-- 1. Get real request data
    user = Depends(get_current_user) # <-- 2. Get real user
):
    """
    Generates outfit suggestions based on user input and their wardrobe.
    """
    try:
        # 3. Fetch the user's REAL wardrobe from Supabase
        user_id = user.id
        data = supabase.table("wardrobe_items").select(
            "item_id", 
            "description", 
            "category", 
            "subcategory",
            "style_tags",
            "formality_level"
        ).eq("owner_id", user_id).execute()
        
        wardrobe = data.data
        if not wardrobe:
            raise HTTPException(status_code=404, detail="Your wardrobe is empty. Please add items first.")

        # 4. Build the Master Prompt
        prompt = OUTFIT_GENERATOR_PROMPT.format(
            occasion=request.occasion,
            style_vibe=request.style_vibe,
            wardrobe_json=json.dumps(wardrobe, indent=2)
        )

        # 5. Call the AI
        response = model.generate_content(prompt)
        
        # 6. Parse the AI's JSON response
        # The model is set to output JSON, so we can parse it directly
        response_json = json.loads(response.text)
        
        return response_json

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to generate outfit: {e}")