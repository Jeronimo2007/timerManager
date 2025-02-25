
from ..database.data import supabase  
from app.services.utils import hash_password


ROLE_CODES = {
    "214389": "socio",
    "132867": "senior",
    "929491": "consultor",
    "224566": "junior",
    "100435": "auxiliar"
}


def create_user(username: str, password: str, role_code: str):
    """ Creates an user with a role """
    hashed_password = hash_password(password)

    
    response = supabase.table("users").insert({
        "username": username,
        "hashed_password": hashed_password,
        "role": role_code  
    }).execute()

    print("Response:", response)
    
    if response.data:
        return {"message": "Usuario creado exitosamente", "user": response.data}
    else:
        return {"error": "Error al crear el usuario", "details": response.error}

def get_user(username: str):
    """ Obtiene los datos de un usuario por su username """
    response = supabase.table("users").select("id,username, hashed_password,role").eq("username", username).execute()
    if response.data:
        return response.data[0]  
    else:
        return None  

