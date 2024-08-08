from fastapi import Depends, HTTPException,APIRouter
from sqlalchemy.orm import Session
from ..logic import user_logic
from ..schemas import user_schema
from ..database import SessionLocal

router = APIRouter()

def get_session_local():
    yield SessionLocal()

@router.get("/users/{user_id}", response_model=user_schema.User)
async def read_user(user_id: int, db: Session = Depends(get_session_local)):
    try:
        user = user_logic.get_user(db, user_id=user_id)
        return user
    except user_logic.UserNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/users/", response_model=user_schema.User)
async def create_user(user: user_schema.UserCreate, db: Session = Depends(get_session_local)):
    return user_logic.create_user(db=db, user=user)

@router.get("/users/", response_model=list[user_schema.User])
async def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_session_local)):
    users = user_logic.get_users(db, skip=skip, limit=limit)
    return users

@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_session_local)):
    user_logic.delete_user(db, user_id=user_id)
    return {"message": "User deleted"}