from fastapi import Depends, HTTPException,APIRouter
from sqlalchemy.orm import Session
from ..logic import album_logic
from ..schemas import album_schema
from ..database import SessionLocal

router = APIRouter()

def get_session_local():
    yield SessionLocal()

@router.post("/users/{user_id}/albums/", response_model=album_schema.Album)
def create_album_for_user(
    user_id: int, album: album_schema.AlbumCreate, db: Session = Depends(get_session_local)):
    return album

@router.get("/albums/{album_id}", response_model=album_schema.Album)
def read_album(album_id: int, db: Session = Depends(get_session_local)):
    db_album = album_logic.get_album(db, album_id=album_id)
    if db_album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    return db_album

@router.delete("/albums/{album_id}", response_model=album_schema.Album)
def delete_album(album_id: int, db: Session = Depends(get_session_local)):
    db_album = album_logic.delete_album(db, album_id=album_id)
    if db_album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    return db_album

@router.get("/users/{user_id}/albums/", response_model=list[album_schema.Album])
def read_albums(user_id: int, db: Session = Depends(get_session_local)):
    albums = album_logic.get_albums_by_user(db, user_id=user_id)
    return albums
