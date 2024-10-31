from sqlmodel import SQLModel, Field
from typing import Optional

class Capture(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    pokemon_name: str
