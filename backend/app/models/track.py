from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from ..database import Base

class Track(Base):
    __tablename__ = "tracks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    minutes = Column(Integer)
    seconds = Column(Integer)
    artist = Column(String, index=True)
    album_id = Column(Integer, ForeignKey("albums.id"))
    album = relationship("Album", back_populates="tracks")