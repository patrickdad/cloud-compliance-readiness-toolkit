from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.services.dashboard_service import get_project_dashboard

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/project/{project_id}")
def get_dashboard(project_id: int, db: Session = Depends(get_db)):
    return get_project_dashboard(project_id, db)