from pydantic import BaseModel
from ..models import Cliente

class Cliente(BaseModel):
    nome: str
    email: str
    telefone: str
    senha: str