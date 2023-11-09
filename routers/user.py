from middlewares.jwt_bearer import JWTBearer
from fastapi import Depends, HTTPException
from models.user import User as UserModel
from services.user import UserService
from config.database import Session
from schemas.user import UserBase
from fastapi import APIRouter

user_router = APIRouter()

# GET users endpoint
@user_router.get('/users', tags=['CRUD'])
def get_users():
    db = Session()
    result = UserService(db).get_users()
    return result

@user_router.get('/users/{id}', tags=['CRUD'])
def get_user_by_id(id: int):
    """ Get user by id """
    db = Session()
    result = UserService(db).get_user_by_id(id)
    if not result:
        raise HTTPException(status_code=404, detail='not found')
    return result

@user_router.get('/users/', tags=['CRUD'])
def get_users_by_address(address: str):
    # filter users by address
    db = Session()
    result = UserService(db).get_user_by_address(address)
    if not result:
        raise HTTPException(status_code=404, detail='not found')
    return result

@user_router.post('/users', tags=['CRUD']) # create route
def create_user(user: UserBase):
    db = Session()
    UserService(db).create_user(user)
    raise HTTPException(status_code=201, detail='user created') # return created status

@user_router.put('/users/{id}', tags=['CRUD'])
def update_user(id: int, user: UserBase):
    """Updates a user with given ID and details."""

    db = Session()
    UserService(db).update_user(id, user) # type: ignore

    raise HTTPException(status_code=200, detail='updated succesfuly')
 
# Retrieve and remove user
@user_router.delete('/users/{id}', tags=['CRUD'], dependencies=[Depends(JWTBearer())])
def delete_user(id: int):

    db = Session()
    UserService(db).delete_user(id)
    raise HTTPException(status_code=200, detail='deleted succesfuly')