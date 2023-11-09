from sqlalchemy import Column, Integer, String
from config.database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String(10), unique=True, nullable=False)
    email = Column(String(50))
    address = Column(String)
    phone = Column(String(13))
    website = Column(String)