from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.user import get_user, get_users, create_user, update_user, delete_user
from app.schemas.user import UserCreate, UserUpdate, User
from app.dependency import get_db
from typing import List

router = APIRouter()

@router.get("/users/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/users/", response_model=User)
def create_user_api(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@router.put("/users/{user_id}", response_model=User)
def update_user_api(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db=db, user_id=user_id, user_update=user)

@router.delete("/users/{user_id}", response_model=User)
def delete_user_api(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db=db, user_id=user_id)
