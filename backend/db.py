import os
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

load_dotenv()

# load DATABASE_URL from your .env (e.g. postgresql+asyncpg://…)
DATABASE_URL = os.getenv('DATABASE_URL')

# echo=True is handy during development
engine = create_engine(DATABASE_URL, echo=True, future=True)

def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session