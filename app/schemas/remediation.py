from pydantic import BaseModel


class RemediationCreate(BaseModel):
    project_id: int
    finding_id: int
    title: str
    description: str | None = None
    owner: str | None = None
    priority: str


class RemediationRead(RemediationCreate):
    id: int
    status: str

    model_config = {"from_attributes": True}