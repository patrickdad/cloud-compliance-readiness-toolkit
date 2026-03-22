from sqlalchemy import Column, ForeignKey, Integer, String, Text
from app.db import Base


class RemediationTask(Base):
    __tablename__ = "remediation_tasks"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    finding_id = Column(Integer, ForeignKey("findings.id"), nullable=False)

    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)

    owner = Column(String(255), nullable=True)
    priority = Column(String(20), nullable=False)
    status = Column(String(50), default="open")