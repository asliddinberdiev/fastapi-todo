from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database import Base
import uuid

class Todo(Base):
    __tablename__ = "todos"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4, nullable=False)
    order = Column(Integer, nullable=False)
    title = Column(String, index=True, nullable=False)
    completed = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))

    items = relationship("Item", back_populates="todo", cascade="all, delete")

class Item(Base):
    __tablename__ = "items"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4, nullable=False)
    todo_id = Column(UUID(as_uuid=True), ForeignKey("todos.id", ondelete="CASCADE"), nullable=False, index=True)
    order = Column(Integer, nullable=False)
    title = Column(String, index=True, nullable=False)
    completed = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))

    todo = relationship("Todo", back_populates="items")
