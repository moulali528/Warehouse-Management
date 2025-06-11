from fastapi import APIRouter
from model_config import TaskRequest
from fastapi import Depends, HTTPException, Path, status
from models import Todos
from db_dependency import DB_DEPENDENCY

router = APIRouter()


@router.get("/tasks", status_code=status.HTTP_200_OK)
async def display_all_tasks(db: DB_DEPENDENCY):
    return db.query(Todos).all()

@router.post("/task/submit", status_code=status.HTTP_201_CREATED)
async def create_task(db: DB_DEPENDENCY, task_details: TaskRequest):
    db_query = Todos(**task_details.model_dump())
    db.add(db_query)
    db.commit()
    return task_details

@router.get('/task/{task_id}')
async def display_task_by_id(db: DB_DEPENDENCY, task_id: int = Path(gt=0)):
    for task in db.query(Todos).all():
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.put("/task/update/{task_id}")
async def update_task_details(db: DB_DEPENDENCY, task_details: TaskRequest, task_id:int = Path(gt=0)):
    task = db.query(Todos).filter(Todos.id == task_id).first()
    if task:
        task.task = task_details.task
        task.description = task_details.description
        task.status = task_details.status
        db.commit()
        return task_details
    raise HTTPException(status_code=404, detail="Task not found")


@router.put("/task/delete/{task_id}")
def delete_task_by_id(db: DB_DEPENDENCY, task_id: int = Path(gt=0)):
    task = db.query(Todos).filter(Todos.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.is_delete = True
    db.commit()
    return {'message': 'Task has been deleted'}