from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.user.UserResponse)
def create_user(user: schemas.user.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.user.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.user.create_user(db, user)