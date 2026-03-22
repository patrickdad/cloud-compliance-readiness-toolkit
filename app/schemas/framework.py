from pydantic import BaseModel


class FrameworkBase(BaseModel):
    name: str
    version: str
    description: str | None = None


class FrameworkCreate(FrameworkBase):
    pass


class FrameworkRead(FrameworkBase):
    id: int

    model_config = {"from_attributes": True}