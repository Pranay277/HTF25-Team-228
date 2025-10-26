from fastapi import APIRouter, HTTPException
from app.core.db import supabase
from app.core.models import UserAuth # <-- Import your new model
from gotrue.errors import AuthApiError  # <-- This is the correct line

router = APIRouter()

@router.post("/signup")
async def signup(user_in: UserAuth):
    """
    Handles new user registration.
    """
    try:
        # Call Supabase to sign the user up
        response = supabase.auth.sign_up({
            "email": user_in.email,
            "password": user_in.password,
        })
        # Supabase returns the full session object (user, token, etc.)
        return response
    
    except AuthApiError as e:
        raise HTTPException(status_code=400, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/login")
async def login(user_in: UserAuth):
    """
    Handles user login and returns a session token.
    """
    try:
        # Call Supabase to sign the user in
        response = supabase.auth.sign_in_with_password({
            "email": user_in.email,
            "password": user_in.password
        })
        # This response contains the access_token the frontend needs
        return response
        
    except AuthApiError as e:
        raise HTTPException(status_code=401, detail=e.message or "Invalid login credentials")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))