from pydantic import BaseModel, Field
from typing import List, Optional
from .track_schema import Track
from ..models.medio import Medio

class AlbumBase(BaseModel):
    title: str
    year: int
    description: Optional[str] = None
    medio: Medio

class AlbumCreate(AlbumBase):
    pass

class Album(AlbumBase):
    id: int
    tracks: List[Track] = []

    class Config:
        orm_mode = True