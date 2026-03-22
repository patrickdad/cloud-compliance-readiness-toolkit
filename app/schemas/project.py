from datetime import datetime
from pydantic import BaseModel


class ProjectBase(BaseModel):
    name: str
    client_name: str
    description: str | None = None
    status: str = "draft"


class ProjectCreate(ProjectBase):
    pass


class ProjectRead(ProjectBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}