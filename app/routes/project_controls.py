from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.control import Control
from app.models.project import Project
from app.models.project_control import ProjectControl
from app.schemas.project_control import (
    ProjectControlCreate,
    ProjectControlRead,
    ProjectControlUpdate,
)

router = APIRouter(prefix="/projects/{project_id}/controls", tags=["Project Controls"])


@router.get("", response_model=list[ProjectControlRead])
def list_project_controls(project_id: int, db: Session = Depends(get_db)):
    return db.query(ProjectControl).filter(ProjectControl.project_id == project_id).all()


@router.post("", response_model=ProjectControlRead)
def add_control_to_project(
        project_id: int,
        payload: ProjectControlCreate,
        db: Session = Depends(get_db),
):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    control = db.query(Control).filter(Control.id == payload.control_id).first()
    if not control:
        raise HTTPException(status_code=404, detail="Control not found")

    project_control = ProjectControl(
        project_id=project_id,
        control_id=payload.control_id,
        owner=payload.owner,
    )
    db.add(project_control)
    db.commit()
    db.refresh(project_control)
    return project_control


@router.patch("/{project_control_id}", response_model=ProjectControlRead)
def update_project_control(
        project_id: int,
        project_control_id: int,
        payload: ProjectControlUpdate,
        db: Session = Depends(get_db),
):
    project_control = (
        db.query(ProjectControl)
        .filter(
            ProjectControl.id == project_control_id,
            ProjectControl.project_id == project_id,
        )
        .first()
    )
    if not project_control:
        raise HTTPException(status_code=404, detail="Project control not found")

    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(project_control, key, value)

    db.commit()
    db.refresh(project_control)
    return project_control
