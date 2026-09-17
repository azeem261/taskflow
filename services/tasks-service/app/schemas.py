from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str = ""


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    owner: str

    class Config:
        from_attributes = True
