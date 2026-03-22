from pydantic import BaseModel


class ControlMappingBase(BaseModel):
    control_id: int
    framework_id: int
    framework_control_code: str
    framework_control_title: str
    mapping_notes: str | None = None


class ControlMappingCreate(ControlMappingBase):
    pass


class ControlMappingRead(ControlMappingBase):
    id: int

    model_config = {"from_attributes": True}