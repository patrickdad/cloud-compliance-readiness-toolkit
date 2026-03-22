from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectRead

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.get("", response_model=list[ProjectRead])
def list_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()


@router.get("/{project_id}", response_model=ProjectRead)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.post("", response_model=ProjectRead)
def create_project(payload: ProjectCreate, db: Session = Depends(get_db)):
    project = Project(**payload.model_dump())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project