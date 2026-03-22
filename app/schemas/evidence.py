from datetime import datetime
from pydantic import BaseModel


class EvidenceCreate(BaseModel):
    project_id: int
    control_id: int
    lab_id: int | None = None
    title: str
    description: str | None = None
    evidence_type: str
    source: str | None = None


class EvidenceRead(EvidenceCreate):
    id: int
    status: str
    collected_at: datetime
    reviewed_by: str | None = None
    file_path: str | None = None
    notes: str | None = None

    model_config = {"from_attributes": True}