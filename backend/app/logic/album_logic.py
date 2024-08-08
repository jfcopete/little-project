from sqlalchemy.orm import Session
from ..repositories import album_repository
from ..schemas import album_schema

def create_album(db: Session, album: album_schema.AlbumCreate, user_id: int):
    """
    Creates a new album.
    """
    return album_repository.create_album(db=db, album=album, user_id=user_id)

def get_album(db: Session, album_id: int):
    """
    Gets an album by id.
    """
    return album_repository.get_album(db=db, album_id=album_id)

def get_albums(db: Session, skip: int = 0, limit: int = 10):
    """
    Gets all albums.
    """
    return album_repository.get_albums(db=db, skip=skip, limit=limit)

def delete_album(db: Session, album_id: int):
    """
    Deletes an album by id.
    """
    db_album = get_album(db=db, album_id=album_id)
    db.delete(db_album)
    db.commit()
    return db_album

def get_albums_by_user(db: Session, user_id: int):
    """
    Gets all albums by user id.
    """
    return db.query(album_schema.Album).filter(album_schema.Album.user_id == user_id).all()

def get_album_by_title(db: Session, title: str):
    """
    Gets an album by title.
    """
    return db.query(album_schema.Album).filter(album_schema.Album.title == title).first
