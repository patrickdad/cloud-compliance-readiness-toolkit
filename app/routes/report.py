from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.control import Control
from app.models.evidence import EvidenceItem
from app.models.finding import Finding
from app.models.project import Project
from app.models.project_control import ProjectControl
from app.models.remediation import RemediationTask
from app.schemas.report import (
    ReadinessReportResponse,
    ReportControlItem,
    ReportEvidenceItem,
    ReportFindingItem,
    ReportProjectInfo,
    ReportRemediationItem,
)
from app.services.dashboard_service import get_project_dashboard

router = APIRouter(prefix="/report", tags=["Report"])


@router.get("/project/{project_id}", response_model=ReadinessReportResponse)
def get_project_report(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    dashboard = get_project_dashboard(project_id, db)

    project_controls = (
        db.query(ProjectControl, Control)
        .join(Control, ProjectControl.control_id == Control.id)
        .filter(ProjectControl.project_id == project_id)
        .all()
    )

    controls = [
        ReportControlItem(
            control_id=control.id,
            control_code=control.control_code,
            control_title=control.title,
            status=project_control.status,
            validation_status=project_control.validation_status,
            readiness_score=project_control.readiness_score,
            owner=project_control.owner,
            implementation_notes=project_control.implementation_notes,
        )
        for project_control, control in project_controls
    ]

    evidence_records = db.query(EvidenceItem).filter(EvidenceItem.project_id == project_id).all()
    evidence = [
        ReportEvidenceItem(
            evidence_id=item.id,
            control_id=item.control_id,
            title=item.title,
            evidence_type=item.evidence_type,
            source=item.source,
            status=item.status,
        )
        for item in evidence_records
    ]

    finding_records = db.query(Finding).filter(Finding.project_id == project_id).all()
    findings = [
        ReportFindingItem(
            finding_id=item.id,
            control_id=item.control_id,
            severity=item.severity,
            title=item.title,
            description=item.description,
            recommendation=item.recommendation,
            status=item.status,
        )
        for item in finding_records
    ]

    remediation_records = db.query(RemediationTask).filter(RemediationTask.project_id == project_id).all()
    remediation_tasks = [
        ReportRemediationItem(
            task_id=item.id,
            finding_id=item.finding_id,
            title=item.title,
            priority=item.priority,
            owner=item.owner,
            status=item.status,
        )
        for item in remediation_records
    ]

    return ReadinessReportResponse(
        project=ReportProjectInfo(
            project_id=project.id,
            project_name=project.name,
            client_name=project.client_name,
            status=project.status,
            description=project.description,
        ),
        dashboard=dashboard,
        controls=controls,
        evidence=evidence,
        findings=findings,
        remediation_tasks=remediation_tasks,
    )