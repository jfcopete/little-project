from sqlalchemy.orm import Session
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

def delete_album(db: Session, album_id: int):
    db_album = get_album(db, album_id)
    db.delete(db_album)
    db.commit()
    return db_album

def get_albums_by_user(db: Session, user_id: int):
    return db.query(Album).filter(Album.user_id == user_id).all()

def get_album_by_title(db: Session, title: str):
    return db.query(Album).filter(Album.title == title).first