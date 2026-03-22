from pydantic import BaseModel


class CrosswalkMappingItem(BaseModel):
    framework_id: int
    framework_name: str
    framework_version: str
    framework_control_code: str
    framework_control_title: str
    mapping_notes: str | None = None


class ControlCrosswalkResponse(BaseModel):
    control_id: int
    control_code: str
    control_title: str
    control_domain: str
    mappings: list[CrosswalkMappingItem]