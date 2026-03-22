from pydantic import BaseModel


class ControlBase(BaseModel):
    control_code: str
    title: str
    description: str
    domain: str
    control_type: str
    priority: str


class ControlCreate(ControlBase):
    pass


class ControlRead(ControlBase):
    id: int

    model_config = {"from_attributes": True}