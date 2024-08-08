from sqlalchemy.orm import Session
from ..repositories import track_repository
from ..schemas import track_schema

def create_track(db: Session, track: track_schema.TrackCreate, album_id: int):
    return track_repository.create_track(db=db, track=track, album_id=album_id)

def get_track(db: Session, track_id: int):
    return track_repository.get_track(db=db, track_id=track_id)

def get_tracks(db: Session, skip: int = 0, limit: int = 10):
    return track_repository.get_tracks(db=db, skip=skip, limit=limit)

def get_tracks_by_album(db: Session, album_id: int):
    return db.query(track_schema.Track).filter(track_schema.Track.album_id == album_id).all()

def delete_track(db: Session, track_id: int):
    db_track = get_track(db=db, track_id=track_id)
    db.delete(db_track)
    db.commit()
    return db_track