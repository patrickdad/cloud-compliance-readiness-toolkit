from sqlalchemy.orm import Session

from app.models.project_control import ProjectControl
from app.models.evidence import EvidenceItem
from app.models.finding import Finding
from app.models.remediation import RemediationTask


def get_project_dashboard(project_id: int, db: Session):
    controls = db.query(ProjectControl).filter(
        ProjectControl.project_id == project_id
    ).all()

    total_controls = len(controls)

    if total_controls == 0:
        readiness = 0
    else:
        validated = len([c for c in controls if c.validation_status == "validated"])
        readiness = round((validated / total_controls) * 100, 2)

    status_breakdown = {
        "not_started": 0,
        "in_progress": 0,
        "implemented": 0,
        "validated": 0,
        "gap_identified": 0,
    }

    for c in controls:
        if c.status in status_breakdown:
            status_breakdown[c.status] += 1

    evidence_count = db.query(EvidenceItem).filter(
        EvidenceItem.project_id == project_id
    ).count()

    findings = db.query(Finding).filter(
        Finding.project_id == project_id
    ).all()

    open_findings = len([f for f in findings if f.status == "open"])

    severity_breakdown = {
        "low": 0,
        "medium": 0,
        "high": 0,
        "critical": 0,
    }

    for f in findings:
        if f.severity in severity_breakdown:
            severity_breakdown[f.severity] += 1

    remediation_tasks = db.query(RemediationTask).filter(
        RemediationTask.project_id == project_id
    ).all()

    open_tasks = len([t for t in remediation_tasks if t.status == "open"])

    return {
        "project_id": project_id,
        "total_controls": total_controls,
        "readiness_percentage": readiness,
        "control_status_breakdown": status_breakdown,
        "evidence_count": evidence_count,
        "open_findings": open_findings,
        "finding_severity_breakdown": severity_breakdown,
        "open_remediation_tasks": open_tasks,
        "readiness_level": (
            "Low" if readiness < 40 else
            "Moderate" if readiness < 70 else
            "High"
        )
    }
