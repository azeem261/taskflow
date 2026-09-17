from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import get_current_owner
from app.database import Base, engine, get_db
from app.models import Task
from app.redis_client import publish_task_event
from app.schemas import TaskCreate, TaskResponse, TaskUpdate

Base.metadata.create_all(bind=engine)

app = FastAPI(title="tasks-service")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tasks", response_model=list[TaskResponse])
def list_tasks(owner: str = Depends(get_current_owner), db: Session = Depends(get_db)):
    return db.query(Task).filter(Task.owner == owner).all()


@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    payload: TaskCreate,
    owner: str = Depends(get_current_owner),
    db: Session = Depends(get_db),
):
    task = Task(title=payload.title, description=payload.description, owner=owner)
    db.add(task)
    db.commit()
    db.refresh(task)
    publish_task_event("task.created", TaskResponse.model_validate(task).model_dump())
    return task


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, owner: str = Depends(get_current_owner), db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id, Task.owner == owner).first()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    payload: TaskUpdate,
    owner: str = Depends(get_current_owner),
    db: Session = Depends(get_db),
):
    task = db.query(Task).filter(Task.id == task_id, Task.owner == owner).first()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(task, field, value)
    db.commit()
    db.refresh(task)
    publish_task_event("task.updated", TaskResponse.model_validate(task).model_dump())
    return task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int, owner: str = Depends(get_current_owner), db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id, Task.owner == owner).first()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    db.delete(task)
    db.commit()
