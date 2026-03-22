from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text
from app.db import Base


class ProjectControl(Base):
    __tablename__ = "project_controls"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    control_id = Column(Integer, ForeignKey("controls.id"), nullable=False)
    status = Column(String(50), nullable=False, default="not_started")
    owner = Column(String(255), nullable=True)
    implementation_notes = Column(Text, nullable=True)
    validation_status = Column(String(50), nullable=False, default="not_validated")
    readiness_score = Column(Float, nullable=False, default=0.0)