from pydantic import BaseModel, Field
from typing import List, Optional
from .track_schema import Track
from ..models.medio import Medios

class AlbumBase(BaseModel):
    title: str
    year: int
    description: Optional[str] = None
    medio: Medios
    tracks: List[Track] = []

class AlbumCreate(AlbumBase):
    pass

class Album(AlbumBase):
    id: int
    usuario_id: int
    tracks: List[Track] = []

    class Config:
        from_attributes = True
        orm_mode = True