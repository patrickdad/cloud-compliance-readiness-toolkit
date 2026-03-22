from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.remediation import RemediationTask
from app.schemas.remediation import RemediationCreate, RemediationRead

router = APIRouter(prefix="/remediation", tags=["Remediation"])


@router.post("", response_model=RemediationRead)
def create_task(payload: RemediationCreate, db: Session = Depends(get_db)):
    task = RemediationTask(**payload.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.get("/project/{project_id}", response_model=list[RemediationRead])
def get_tasks(project_id: int, db: Session = Depends(get_db)):
    return db.query(RemediationTask).filter(RemediationTask.project_id == project_id).all()