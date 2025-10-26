from pydantic import BaseModel
from typing import List, Optional

# This defines the JSON the frontend MUST send
class GenerateRequest(BaseModel):
    occasion: str
    style_vibe: str
    weather: Optional[str] = None # Optional field

# This defines the JSON your API will send back
class OutfitSuggestion(BaseModel):
    outfit_items: List[str] # A list of item_ids (UUIDs)
    explanation: str
    tip: str

class OutfitResponse(BaseModel):
    root: List[OutfitSuggestion]
# ... (keep the other classes)

class UserAuth(BaseModel):
    email: str
    password: str