from sqlalchemy import Column, ForeignKey, Integer, String, Text
from app.db import Base


class ControlMapping(Base):
    __tablename__ = "control_mappings"

    id = Column(Integer, primary_key=True, index=True)
    control_id = Column(Integer, ForeignKey("controls.id"), nullable=False)
    framework_id = Column(Integer, ForeignKey("frameworks.id"), nullable=False)
    framework_control_code = Column(String(100), nullable=False)
    framework_control_title = Column(String(255), nullable=False)
    mapping_notes = Column(Text, nullable=True)