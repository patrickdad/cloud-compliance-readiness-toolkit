from pydantic import BaseModel


class ReportProjectInfo(BaseModel):
    project_id: int
    project_name: str
    client_name: str
    status: str
    description: str | None = None


class ReportControlItem(BaseModel):
    control_id: int
    control_code: str
    control_title: str
    status: str
    validation_status: str
    readiness_score: float
    owner: str | None = None
    implementation_notes: str | None = None


class ReportEvidenceItem(BaseModel):
    evidence_id: int
    control_id: int
    title: str
    evidence_type: str
    source: str | None = None
    status: str


class ReportFindingItem(BaseModel):
    finding_id: int
    control_id: int
    severity: str
    title: str
    description: str
    recommendation: str | None = None
    status: str


class ReportRemediationItem(BaseModel):
    task_id: int
    finding_id: int
    title: str
    priority: str
    owner: str | None = None
    status: str


class ReadinessReportResponse(BaseModel):
    project: ReportProjectInfo
    dashboard: dict
    controls: list[ReportControlItem]
    evidence: list[ReportEvidenceItem]
    findings: list[ReportFindingItem]
    remediation_tasks: list[ReportRemediationItem]