from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.finding import Finding
from app.schemas.finding import FindingCreate, FindingRead

router = APIRouter(prefix="/findings", tags=["Findings"])


@router.post("", response_model=FindingRead)
def create_finding(payload: FindingCreate, db: Session = Depends(get_db)):
    finding = Finding(**payload.model_dump())
    db.add(finding)
    db.commit()
    db.refresh(finding)
    return finding


@router.get("/project/{project_id}", response_model=list[FindingRead])
def get_project_findings(project_id: int, db: Session = Depends(get_db)):
    return db.query(Finding).filter(Finding.project_id == project_id).all()