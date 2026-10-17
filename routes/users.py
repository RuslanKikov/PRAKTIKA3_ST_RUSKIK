from fastapi import APIRouter, HTTPException, status
from models.users import NewUser, UserSignIn

user_router = APIRouter(tags=["User"])
users = {}


@user_router.post("/signup")
async def sign_new_user(data: NewUser) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь с таким email уже существует"
        )
    users[data.email] = data
    return {"message": "Пользователь успешно зарегистрирован (Руслан Киков)"}


@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь не существует"
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Неверные учетные данные"
        )
    return {"message": "Пользователь успешно вошел (Руслан Киков)"}


