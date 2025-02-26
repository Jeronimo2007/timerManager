from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

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
