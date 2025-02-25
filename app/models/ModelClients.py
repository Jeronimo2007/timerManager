from app.database.data import supabase



def create_client(name: str, color: str):
    
    response = supabase.table('clients').insert({
        'name': name,
        'color': color
    }).execute()

    if response.data:
        return {"message": "Usuario creado exitosamente", "user": response.data}
    else:
        return {"error": "Error al crear el usuario", "details": response.error}
    


def read_clients():

    response = supabase.table('clients').select('*').execute()


    return response.data

