from pydantic import BaseModel, Field

class User(BaseModel):
    email: str = Field(default='admin') # Represents user's email
    password: str = Field(default='admin') # Stores user's password