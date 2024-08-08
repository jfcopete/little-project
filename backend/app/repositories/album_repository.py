from sqlalchemy import Session
from ..models.album import Album
from ..schemas.album_schema import AlbumCreate

def get_album(db: Session, album_id: int):
    return db.query(Album).filter(Album.id == album_id).first()

def get_albums(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Album).offset(skip).limit(limit).all

def create_album(db: Session, album: AlbumCreate, user_id:int):
    db_album = Album(**album.dict(), user_id=user_id)
    db.add(db_album)
    db.commit()
    db.refresh(db_album)
    return db_album