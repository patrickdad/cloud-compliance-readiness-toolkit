from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.framework import Framework
from app.schemas.framework import FrameworkCreate, FrameworkRead

router = APIRouter(prefix="/frameworks", tags=["Frameworks"])


@router.get("", response_model=list[FrameworkRead])
def list_frameworks(db: Session = Depends(get_db)):
    return db.query(Framework).all()


@router.post("", response_model=FrameworkRead)
def create_framework(payload: FrameworkCreate, db: Session = Depends(get_db)):
    framework = Framework(**payload.model_dump())
    db.add(framework)
    db.commit()
    db.refresh(framework)
    return framework