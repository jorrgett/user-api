from models.user import User as UserModel
from schemas.user import UserBase
from fastapi import HTTPException

class UserService():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_users(self):
        result = self.db.query(UserModel).all()
        return result
    
    def get_user_by_id(self, id):
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        return result
    
    def get_user_by_address(self, address):
        result = self.db.query(UserModel).filter(UserModel.address == address).all()
        return result
    
    def create_user(self, user: UserBase):
        user_exists = self.db.query(UserModel).filter(UserModel.username == user.username).first()

        if user_exists:
            raise HTTPException(status_code=409, detail='user already exists')
        
        new_user = UserModel(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        return
    
    def update_user(self, id: int, data: UserModel):
        existing_user = self.db.query(UserModel).filter(UserModel.id == id).first()

        if not existing_user:
            raise HTTPException(status_code=404, detail="User doesn't exist")

        existing_user.name = data.name  # type: ignore
        existing_user.username = data.username  # type: ignore
        existing_user.email = data.email  # type: ignore
        existing_user.address = data.address  # type: ignore
        existing_user.phone = data.phone  # type: ignore
        existing_user.website = data.website  # type: ignore

        self.db.commit()
        return
    
    def delete_user(self, id: int):
        existing_user = self.db.query(UserModel).filter(UserModel.id == id).first()

        if not existing_user:
            raise HTTPException(status_code=404, detail="User doesn't exist")
        
        self.db.delete(existing_user)
        self.db.commit()