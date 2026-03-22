from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.evidence import EvidenceItem
from app.schemas.evidence import EvidenceCreate, EvidenceRead

router = APIRouter(prefix="/evidence", tags=["Evidence"])


@router.post("", response_model=EvidenceRead)
def create_evidence(payload: EvidenceCreate, db: Session = Depends(get_db)):
    evidence = EvidenceItem(**payload.model_dump())
    db.add(evidence)
    db.commit()
    db.refresh(evidence)
    return evidence


@router.get("/project/{project_id}", response_model=list[EvidenceRead])
def get_project_evidence(project_id: int, db: Session = Depends(get_db)):
    return db.query(EvidenceItem).filter(EvidenceItem.project_id == project_id).all()