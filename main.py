from uuid import UUID

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import repository
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="ToDo API with Items")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/todos", response_model=list[schemas.TodoOut])
def read_todos(db: Session = Depends(get_db)):
    return repository.get_todos(db)


@app.get("/todos/{todo_id}", response_model=schemas.TodoOut)
def read_todo(todo_id: UUID, db: Session = Depends(get_db)):
    todo = repository.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.post("/todos", response_model=schemas.TodoOut)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return repository.create_todo(db, todo)


@app.put("/todos/{todo_id}", response_model=schemas.TodoOut)
def update_todo(todo_id: UUID, todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
    updated = repository.update_todo(db, todo_id, todo)
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: UUID, db: Session = Depends(get_db)):
    deleted = repository.delete_todo(db, todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"detail": "Todo deleted"}


@app.get("/todos/{todo_id}/items", response_model=list[schemas.ItemOut])
def read_items(todo_id: UUID, db: Session = Depends(get_db)):
    return repository.get_items_by_todo(db, todo_id)


@app.post("/todos/{todo_id}/items", response_model=schemas.ItemOut)
def create_item(todo_id: UUID, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return repository.create_item(db, todo_id, item)


@app.put("/items/{item_id}", response_model=schemas.ItemOut)
def update_item(item_id: UUID, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
    updated = repository.update_item(db, item_id, item)
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated


@app.delete("/items/{item_id}")
def delete_item(item_id: UUID, db: Session = Depends(get_db)):
    deleted = repository.delete_item(db, item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted"}


if __name__ == "__main__":
    import uvicorn
    from config import settings

    uvicorn.run("main:app", host=settings.APP_HOST, port=settings.APP_PORT, reload=settings.APP_RELOAD)