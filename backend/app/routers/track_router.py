from fastapi import Depends, HTTPException,APIRouter
from sqlalchemy.orm import Session
from ..logic import track_logic
from ..schemas import track_schema
from ..database import SessionLocal

router = APIRouter()

def get_session_local():
    yield SessionLocal()

@router.post("/albums/{album_id}/tracks/", response_model=track_schema.TrackCreate)
def create_track_for_album(
    album_id: int, track: track_schema.TrackCreate, db: Session = Depends(get_session_local)):
    return track_logic.create_track(db=db, track=track, album_id=album_id)

@router.get("/tracks/{track_id}", response_model=track_schema.Track)
def read_track(track_id: int, db: Session = Depends(get_session_local)):
    db_track = track_logic.get_track(db, track_id=track_id)
    if db_track is None:
        raise HTTPException(status_code=404, detail="Track not found")
    return db_track

@router.delete("/tracks/{track_id}", response_model=track_schema.Track)
def delete_track(track_id: int, db: Session = Depends(get_session_local)):
    db_track = track_logic.delete_track(db, track_id=track_id)
    if db_track is None:
        raise HTTPException(status_code=404, detail="Track not found")
    return db_track

@router.get("/albums/{album_id}/tracks/", response_model=list[track_schema.Track])
def read_tracks(album_id: int, db: Session = Depends(get_session_local)):
    tracks = track_logic.get_tracks_by_album(db, album_id=album_id)
    return tracks