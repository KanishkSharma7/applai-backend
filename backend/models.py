from sqlmodel import SQLModel, Field
from datetime import datetime

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str | None = Field(default=None, index=True)
    password: str
    created_at: datetime = Field(default_factory=datetime.now)