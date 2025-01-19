from fastapi import FastAPI, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models

app = FastAPI()


class TasksBase(BaseModel):
    name: str
    is_done: bool
    deadline: str


class TasksModel(TasksBase):
    id: int

    class Config:
        orm_mode = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependancy = Annotated[Session, Depends(get_db)]
models.Base.metadata.create_all(bind=engine)


@app.post("/tasks", response_model=TasksModel)
async def create_task(tasks: TasksBase, db: db_dependancy):
    db_tasks = models.Tasks(**tasks.model_dump())
    db.add(db_tasks)
    db.commit()
    db.refresh(db_tasks)
    return db_tasks


@app.get("/tasks", response_model=List[TasksModel])
async def read_tasks(db: db_dependancy, skip: int = 0, limit: int = 100):
    tasks = db.query(models.Tasks).offset(skip).limit(limit).all()
    return tasks
