from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from utils.jwt_manager import validate_token

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        # Verify and retrieve token
        auth = await super().__call__(request)
        
        # Validate and extract token data
        data = validate_token(auth.credentials) # type: ignore
        
        # Check if email is "admin"
        if data['email'] != "admin":
            # Raise HTTP exception if not
            raise HTTPException(status_code=403, detail="You don't have permissions")