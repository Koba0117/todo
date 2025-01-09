from sqlalchemy import Boolean, Column, Integer, String

from database import Base


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    is_done = Column(Boolean)
    deadline = Column(String, nullable=True)
