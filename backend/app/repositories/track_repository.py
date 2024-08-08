from sqlalchemy import Session
from ..models.track import Track
from ..schemas.track_schema import TrackCreate

def get_track(db: Session, track_id: int):
    return db.query(Track).filter(Track.id == track_id).first()

def get_tracks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Track).offset(skip).limit(limit).all

def create_track(db: Session, track: TrackCreate, album_id: int):
    db_track = Track(**track.dict(),album_id=album_id)
    db.add(db_track)
    db.commit()
    db.refresh(db_track)
    return db_track