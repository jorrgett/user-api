from middlewares.error_handler import ErrorHandler
from config.database import engine, Base
from routers.user import user_router
from routers.auth import auth_router
from fastapi import FastAPI
import uvicorn

app = FastAPI(title='Users API', version='1.0.0')

app.add_middleware(ErrorHandler)

app.include_router(auth_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)

# GET method on home page
@app.get('/', tags=['HOME'])
def home():
    return {"message":"Users API"} # Users API response

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)