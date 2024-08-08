from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from ..database import Base
from .medio import Medios

class Album(Base):
    __tablename__ = "albums"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year = Column(Integer)
    description = Column(String)
    medio = Column(Enum(Medios))
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="albums")
    tracks = relationship("Track", back_populates="album")