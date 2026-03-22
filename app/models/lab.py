from sqlalchemy import Column, Integer, String, Text
from app.db import Base


class Lab(Base):
    __tablename__ = "labs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    cloud_provider = Column(String(50), nullable=False)
    execution_type = Column(String(50), nullable=False)
    evidence_type = Column(String(50), nullable=False)