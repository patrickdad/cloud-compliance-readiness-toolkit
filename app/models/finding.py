from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from app.db import Base


class Finding(Base):
    __tablename__ = "findings"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    control_id = Column(Integer, ForeignKey("controls.id"), nullable=False)

    severity = Column(String(20), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    recommendation = Column(Text, nullable=True)

    status = Column(String(50), default="open")
    created_at = Column(DateTime, default=datetime.utcnow)