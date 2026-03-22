from pydantic import BaseModel


class ProjectControlCreate(BaseModel):
    control_id: int
    owner: str | None = None


class ProjectControlUpdate(BaseModel):
    status: str | None = None
    owner: str | None = None
    implementation_notes: str | None = None
    validation_status: str | None = None
    readiness_score: float | None = None


class ProjectControlRead(BaseModel):
    id: int
    project_id: int
    control_id: int
    status: str
    owner: str | None = None
    implementation_notes: str | None = None
    validation_status: str
    readiness_score: float

    model_config = {"from_attributes": True}