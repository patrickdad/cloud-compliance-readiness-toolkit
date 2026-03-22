from datetime import datetime
from pydantic import BaseModel


class FindingCreate(BaseModel):
    project_id: int
    control_id: int
    severity: str
    title: str
    description: str
    recommendation: str | None = None


class FindingRead(FindingCreate):
    id: int
    status: str
    created_at: datetime

    model_config = {"from_attributes": True}