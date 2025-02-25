from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, clientes

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los headers
)


app.include_router(auth.router)
app.include_router(clientes.router)

@app.get('/')
def root():
    pass