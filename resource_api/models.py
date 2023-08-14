from pydantic import BaseModel


class User(BaseModel):
    id: str


class Resource(BaseModel):
    title: str
