from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import api_router  # no leading space here

app = FastAPI(title="AI Outfit Planner API")

# --- CORS Middleware ---
# This is critical for letting the React Native app talk to your backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the AI Outfit Planner API!"}

# --- Include your API routes ---
app.include_router(api_router, prefix="/api")  # no leading space here
