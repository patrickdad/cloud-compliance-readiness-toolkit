from pydantic import BaseModel


class LabBase(BaseModel):
    name: str
    description: str
    cloud_provider: str
    execution_type: str
    evidence_type: str


class LabCreate(LabBase):
    pass


class LabRead(LabBase):
    id: int

    model_config = {"from_attributes": True}