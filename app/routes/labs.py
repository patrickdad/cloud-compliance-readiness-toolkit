from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.lab import Lab
from app.schemas.lab import LabCreate, LabRead

router = APIRouter(prefix="/labs", tags=["Labs"])


@router.get("", response_model=list[LabRead])
def list_labs(db: Session = Depends(get_db)):
    return db.query(Lab).all()


@router.post("", response_model=LabRead)
def create_lab(payload: LabCreate, db: Session = Depends(get_db)):
    lab = Lab(**payload.model_dump())
    db.add(lab)
    db.commit()
    db.refresh(lab)
    return lab