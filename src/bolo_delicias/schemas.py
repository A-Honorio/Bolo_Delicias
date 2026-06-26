from pydantic import BaseModel, EmailStr

class Cliente(BaseModel):
    nome: str
    email: EmailStr
    telefone: str
    senha: str

class ClienteResponse(BaseModel):
    id: int
    nome: str
    email: str
    telefone: str

    class Config:
        from_attributes = True

class Carrinho(BaseModel):
    cliente_id: int
    produto: str
    quantidade: int

class CarrinhoResponse(BaseModel):
    id: int
    cliente_id: int
    produto: str
    quantidade: int

    class Config:
        from_attributes = True