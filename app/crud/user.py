from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app import models, schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_username(db: Session, username: str):
    return db.query(models.user.User).filter(models.user.User.username == username).first()

def create_user(db: Session, user: schemas.user.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.user.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user