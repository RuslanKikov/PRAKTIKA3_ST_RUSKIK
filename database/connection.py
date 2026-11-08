from sqlmodel import SQLModel, Session, create_engine
from models.events import Event

database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"
connect_args = {"check_same_thread": False}

# echo=True будет выводить все SQL-запросы в консоль (удобно для отладки)
engine_url = create_engine(database_connection_string, echo=True, connect_args=connect_args)

def conn():
    # Создает файл БД и таблицы, если их нет
    SQLModel.metadata.create_all(engine_url)

def get_session():
    # Выдает сессию для работы с БД и закрывает её после завершения
    with Session(engine_url) as session:
        yield session
