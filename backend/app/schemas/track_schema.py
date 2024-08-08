# Suggested code may be subject to a license. Learn more: ~LicenseLog:757152362.
from pydatic import BaseModel
from typing import List

class TrackBase(BaseModel):
    title: str
    minutess: int
    seconds: int
    artist: str

class TrackCreate(TrackBase):
    pass

class Track(TrackBase):
    id: int
    album_id: int

    class Config:
        from_attributes = True
        orm_mode = True