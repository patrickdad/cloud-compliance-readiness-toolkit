from sqlalchemy import Column, Integer, String, Text
from app.db import Base


class Framework(Base):
    __tablename__ = "frameworks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    version = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)