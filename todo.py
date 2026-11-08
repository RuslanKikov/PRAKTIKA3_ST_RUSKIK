from fastapi import APIRouter, Path, HTTPException, status, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from model import Todo, TodoItem, TodoItems


todo_router = APIRouter()
todo_list = []

templates = Jinja2Templates(directory="templates")


@todo_router.post("/todo", status_code=201)
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse(
        request=request,
        name="todo.html",
        context={"todos": todo_list}
    )


@todo_router.get("/todo")
async def retrieve_todos(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="todo.html",
        context={"todos": todo_list}
    )


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(
    request: Request,
    todo_id: int = Path(..., title="ID задачи для получения")
):
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse(
                request=request,
                name="todo.html",
                context={"todo": todo}
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задачи с таким ID не существует (Руслан Киков)"
    )


@todo_router.put("/todo/{todo_id}")
async def update_todo(
    todo_data: TodoItem,
    todo_id: int = Path(..., title="ID задачи для обновления")
):
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {"message": "Задача обновлена Русланом Киковым"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задачи с таким ID не существует (Руслан Киков)"
    )


@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(
    todo_id: int = Path(..., title="ID задачи для удаления")
):
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {"message": "Задача удалена Русланом Киковым"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задачи с таким ID не существует (Руслан Киков)"
    )


@todo_router.delete("/todo")
async def delete_all_todos():
    todo_list.clear()
    return {"message": "Все задачи удалены Русланом Киковым"}
