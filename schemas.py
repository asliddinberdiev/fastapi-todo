from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, List

class ItemBase(BaseModel):
    title: str
    order: int
    completed: Optional[bool] = False

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    completed: bool

class ItemOut(ItemBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True

class TodoBase(BaseModel):
    title: str
    order: int
    completed: Optional[bool] = False

class TodoCreate(TodoBase):
    items: Optional[List[ItemCreate]] = []

class TodoUpdate(TodoBase):
    completed: bool

class TodoOut(TodoBase):
    id: UUID
    created_at: datetime
    items: List[ItemOut] = []

    class Config:
        orm_mode = True
