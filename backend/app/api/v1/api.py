from fastapi import APIRouter
from app.api.v1.endpoints import outfits
from app.api.v1.endpoints import wardrobe
from app.api.v1.endpoints import auth

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(outfits.router, prefix="/outfits", tags=["Outfits"])
api_router.include_router(wardrobe.router, prefix="/wardrobe", tags=["Wardrobe"])
# We will add wardrobe.router here later