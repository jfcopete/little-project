from sqlalchemy.orm import Session
from ..repositories import user_repository
from ..schemas import user_schema

class UserNotFound(Exception):
       def __init__(self, user_id: int):
           self.message = f"User with ID {user_id} not found"
           super().__init__(self.message)

def get_user(db: Session, user_id: int) -> bool:
    db_user = user_repository.get_user(db, user_id=user_id)
    if db_user is None:
        raise UserNotFound(user_id)
    return user_schema.User.from_orm(db_user)

def create_user(db: Session, user: user_schema.UserCreate) -> user_schema.User:
    db_user = user_repository.create_user(db, user)
    return user_schema.User.from_orm(db_user)

def get_users(db: Session, skip: int = 0, limit: int = 10):
    db_users = user_repository.get_users(db, skip=skip, limit=limit)
    return [user_schema.User.from_orm(db_user) for db_user in db_users]

def delete_user(db: Session, user_id: int):
    user_repository.delete_user(db, user_id=user_id)
    return True