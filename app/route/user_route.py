from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.user_schemas import UserCreate
from app.models.database import get_db
from app.crud_function.Create_user_data.create_user import Create_user_data,get_all_user
from app.schemas.user_schemas import ShowUser

router = APIRouter(prefix="/User", tags=["UserData"])


@router.post("/")
def create_user(request: UserCreate, db: Session = Depends(get_db)):
    return Create_user_data(request, db)


@router.get("/", response_model=List[ShowUser])
def show_user(db: Session = Depends(get_db)):
    return get_all_user(db)
