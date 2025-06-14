from sqlalchemy.orm import Session
from models import Todo, Item
from schemas import TodoCreate, TodoUpdate, ItemCreate, ItemUpdate
from uuid import UUID

def get_todos(db: Session):
    return db.query(Todo).all()

def get_todo(db: Session, todo_id: UUID):
    return db.query(Todo).filter(Todo.id == todo_id).first()

def create_todo(db: Session, todo: TodoCreate):
    db_todo = Todo(
        title=todo.title,
        order=todo.order,
        completed=todo.completed
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)

    for item in todo.items:
        db_item = Item(
            title=item.title,
            order=item.order,
            completed=item.completed,
            todo_id=db_todo.id
        )
        db.add(db_item)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: UUID, updated_data: TodoUpdate):
    todo = get_todo(db, todo_id)
    if not todo:
        return None
    for key, value in updated_data.dict().items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo

def delete_todo(db: Session, todo_id: UUID):
    todo = get_todo(db, todo_id)
    if not todo:
        return None
    db.delete(todo)
    db.commit()
    return todo

def get_items_by_todo(db: Session, todo_id: UUID):
    return db.query(Item).filter(Item.todo_id == todo_id).all()

def get_item(db: Session, item_id: UUID):
    return db.query(Item).filter(Item.id == item_id).first()

def create_item(db: Session, todo_id: UUID, item: ItemCreate):
    db_item = Item(
        title=item.title,
        order=item.order,
        completed=item.completed,
        todo_id=todo_id
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id: UUID, updated_data: ItemUpdate):
    item = get_item(db, item_id)
    if not item:
        return None
    for key, value in updated_data.dict().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

def delete_item(db: Session, item_id: UUID):
    item = get_item(db, item_id)
    if not item:
        return None
    db.delete(item)
    db.commit()
    return item
