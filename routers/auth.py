from fastapi import APIRouter, HTTPException
from utils.jwt_manager import create_token
from schemas.auth import User

auth_router = APIRouter()

# Route to handle login
@auth_router.post('/login', tags=['AUTH'])
def login(user: User):
    # Check if the provided credentials match the admin account
    if user.email == "admin" and user.password == "admin":
        # Create a JWT token using the provided user information
        token: str = create_token(user.dict())
        # Return the JWT token with a 200 status code
        raise HTTPException(status_code=200, detail=token)