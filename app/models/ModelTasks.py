

from datetime import datetime
from typing import Optional
from app.database.data import supabase

from app.schemas.schemas import TaskCreate, TaskUpdate



def format_datetime(dt: Optional[datetime]) -> Optional[str]:
    """ Convierte un objeto datetime a string en formato ISO 8601 """
    return dt.isoformat() if dt else None


def create_task(task_data: TaskCreate):

    """ creates a new task in the database """

    task_dict = task_data.dict()
    task_dict["due_date"] = format_datetime(task_data.due_date)

    response = supabase.table("tasks").insert(task_dict).execute()

    if response.data:

        return response.data[0]
    
    else:

        return {"error": response.error}


def get_all_tasks():

    """ get all the tasks """

    response = supabase.table("tasks").select("*").execute()

    return response.data if response.data else []


def get_tasks_by_user_id(user_id: int):

    """ get a task by user id """

    response = supabase.table("tasks").select("*").eq("assigned_to_id", user_id).execute()

    return response.data


def update_task(task_id: int, task_data: TaskUpdate):

    """ update a task by id """
    task_dict = task_data.dict()
    task_dict["due_date"] = format_datetime(task_data.due_date)

    response = supabase.table("tasks").update(task_data.dict(exclude_unset=True)).eq("id", task_id).execute()

    if response.data:

        return response.data[0]
    
    else:

        return {"error": response.error}
    

def delete_task(task_id: int):

    """ remove a tasks """

    response = supabase.table("tasks").delete().eq("id", task_id).execute()

    if response.data:

        return {"message": "Tarea eliminada correctamente"}
    
    else:

        return {"error": response.error}