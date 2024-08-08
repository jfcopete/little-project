from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=False)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    albums = relationship("Album", back_populates="user")