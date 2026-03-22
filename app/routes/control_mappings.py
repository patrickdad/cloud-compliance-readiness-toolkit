from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.control import Control
from app.models.control_mapping import ControlMapping
from app.models.framework import Framework
from app.schemas.control_mapping import ControlMappingCreate, ControlMappingRead

router = APIRouter(prefix="/control-mappings", tags=["Control Mappings"])


@router.post("", response_model=ControlMappingRead)
def create_control_mapping(payload: ControlMappingCreate, db: Session = Depends(get_db)):
    control = db.query(Control).filter(Control.id == payload.control_id).first()
    if not control:
        raise HTTPException(status_code=404, detail="Control not found")

    framework = db.query(Framework).filter(Framework.id == payload.framework_id).first()
    if not framework:
        raise HTTPException(status_code=404, detail="Framework not found")

    mapping = ControlMapping(**payload.model_dump())
    db.add(mapping)
    db.commit()
    db.refresh(mapping)
    return mapping


@router.get("", response_model=list[ControlMappingRead])
def list_control_mappings(db: Session = Depends(get_db)):
    return db.query(ControlMapping).all()


@router.get("/control/{control_id}", response_model=list[ControlMappingRead])
def get_mappings_for_control(control_id: int, db: Session = Depends(get_db)):
    return db.query(ControlMapping).filter(ControlMapping.control_id == control_id).all()


@router.get("/framework/{framework_id}", response_model=list[ControlMappingRead])
def get_mappings_for_framework(framework_id: int, db: Session = Depends(get_db)):
    return db.query(ControlMapping).filter(ControlMapping.framework_id == framework_id).all()