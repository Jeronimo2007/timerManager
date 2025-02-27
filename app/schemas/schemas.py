from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class clientCreate(BaseModel):
    name: str
    color: str


class clientUpdate(BaseModel):
    name: str
    color: str



class clientDelete(BaseModel):
    id: int


class TaskCreate(BaseModel):
    client_id: int
    title: str = Field(..., min_length=3, max_length=255)
    description: Optional[str] = None
    assigned_to_id: int
    due_date: datetime

class TaskUpdate(BaseModel):
    description: Optional[str] = None
    status: Optional[str] = None
    due_date: Optional[datetime] = None

class TaskResponse(BaseModel):
    id: int
    client_id: int
    title: str
    description: Optional[str]
    assigned_to_id: int
    status: str
    assignment_date: datetime
    due_date: Optional[datetime]
    total_time: float


class TimeEntryCreate(BaseModel):
    task_id: int
    start_time: datetime
    end_time: datetime


class TimeEntryUpdate(BaseModel):
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None


class TimeEntryResponse(BaseModel):
    id: int
    task_id: int
    user_id: int
    start_time: datetime
    end_time: datetime
    duration: float