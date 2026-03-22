from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.control import Control
from app.schemas.control import ControlCreate, ControlRead

router = APIRouter(prefix="/controls", tags=["Controls"])


@router.get("", response_model=list[ControlRead])
def list_controls(db: Session = Depends(get_db)):
    return db.query(Control).all()


@router.get("/{control_id}", response_model=ControlRead)
def get_control(control_id: int, db: Session = Depends(get_db)):
    control = db.query(Control).filter(Control.id == control_id).first()
    if not control:
        raise HTTPException(status_code=404, detail="Control not found")
    return control


@router.post("", response_model=ControlRead)
def create_control(payload: ControlCreate, db: Session = Depends(get_db)):
    control = Control(**payload.model_dump())
    db.add(control)
    db.commit()
    db.refresh(control)
    return control