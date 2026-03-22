from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from app.db import Base


class EvidenceItem(Base):
    __tablename__ = "evidence_items"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    control_id = Column(Integer, ForeignKey("controls.id"), nullable=False)
    lab_id = Column(Integer, ForeignKey("labs.id"), nullable=True)

    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)

    evidence_type = Column(String(50), nullable=False)
    source = Column(String(100), nullable=True)

    status = Column(String(50), default="collected")

    collected_at = Column(DateTime, default=datetime.utcnow)
    reviewed_by = Column(String(255), nullable=True)

    file_path = Column(String(255), nullable=True)
    notes = Column(Text, nullable=True)