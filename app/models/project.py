from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text
from app.db import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    client_name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(50), nullable=False, default="draft")
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)