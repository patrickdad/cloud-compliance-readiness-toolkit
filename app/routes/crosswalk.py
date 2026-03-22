from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.control import Control
from app.models.control_mapping import ControlMapping
from app.models.framework import Framework
from app.schemas.crosswalk import ControlCrosswalkResponse, CrosswalkMappingItem

router = APIRouter(prefix="/crosswalk", tags=["Crosswalk"])


@router.get("/control/{control_id}", response_model=ControlCrosswalkResponse)
def get_control_crosswalk(control_id: int, db: Session = Depends(get_db)):
    control = db.query(Control).filter(Control.id == control_id).first()
    if not control:
        raise HTTPException(status_code=404, detail="Control not found")

    mappings = (
        db.query(ControlMapping, Framework)
        .join(Framework, ControlMapping.framework_id == Framework.id)
        .filter(ControlMapping.control_id == control_id)
        .all()
    )

    mapping_items = [
        CrosswalkMappingItem(
            framework_id=framework.id,
            framework_name=framework.name,
            framework_version=framework.version,
            framework_control_code=mapping.framework_control_code,
            framework_control_title=mapping.framework_control_title,
            mapping_notes=mapping.mapping_notes,
        )
        for mapping, framework in mappings
    ]

    return ControlCrosswalkResponse(
        control_id=control.id,
        control_code=control.control_code,
        control_title=control.title,
        control_domain=control.domain,
        mappings=mapping_items,
    )