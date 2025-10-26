import os
from supabase import create_client, Client
from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.config import SUPABASE_URL, SUPABASE_KEY

# 1. Create the Supabase Client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# 2. Define the authentication dependency
auth_scheme = HTTPBearer()

def get_current_user(token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    """
    A dependency to get the current user from their Supabase auth token.
    """
    try:
        # Get the raw JWT string
        jwt = token.credentials

        # Validate the token and get user data
        user_data = supabase.auth.get_user(jwt)

        # Return the user object
        return user_data.user
    except Exception as e:
        print(e) # Log the error
        raise HTTPException(
            status_code=401, 
            detail="Invalid or expired authentication token"
        )