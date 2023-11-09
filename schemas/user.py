from pydantic import BaseModel, Field

class UserBase(BaseModel):
    name: str # User's full name
    username: str = Field(min_length=5) # User's unique username
    email: str # User's email address
    address: str # User's mailing address
    phone: str = Field(max_length=13) # User's phone number
    website: str # User's personal website