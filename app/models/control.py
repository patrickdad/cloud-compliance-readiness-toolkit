from sqlalchemy import Column, Integer, String, Text
from app.db import Base


class Control(Base):
    __tablename__ = "controls"

    id = Column(Integer, primary_key=True, index=True)
    control_code = Column(String(50), nullable=False, unique=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    domain = Column(String(100), nullable=False)
    control_type = Column(String(50), nullable=False)
    priority = Column(String(20), nullable=False)