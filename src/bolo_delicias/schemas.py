from pydantic import BaseModel, EmailStr


# Dados recebidos ao cadastrar cliente
class ClienteCreate(BaseModel):
    nome: str
    email: EmailStr
    telefone: str
    senha: str


# Dados retornados pela API
class ClienteResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
    telefone: str

    class Config:
        from_attributes = True


# Carrinho
class CarrinhoItemCreate(BaseModel):
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