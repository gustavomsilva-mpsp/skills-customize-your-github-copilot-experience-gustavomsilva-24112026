from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    title: str
    completed: bool = False


tasks: list[dict] = []


@app.get("/")
def read_root():
    # Retorne uma mensagem indicando que a API está funcionando.
    pass


@app.post("/tasks")
def create_task(task: Task):
    # Crie um novo registro com um identificador, adicione-o à lista e retorne-o.
    pass


@app.get("/tasks")
def list_tasks():
    # Retorne todas as tarefas.
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # Encontre uma tarefa pelo identificador ou lance HTTPException com status 404.
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # Remova a tarefa pelo identificador ou lance HTTPException com status 404.
    pass
