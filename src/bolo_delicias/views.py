from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .database import get_db
from . import schemas
from .services import cliente_service
from .services import carrinho_service
from .services import checkout_service

router = APIRouter()

# 1. Rota para Cadastrar Cliente
@router.post("/clientes/", response_model=schemas.ClienteResponse, status_code=status.HTTP_201_CREATED)
def criar_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    db_cliente = cliente_service.obter_cliente_por_email(db, email=cliente.email)
    if db_cliente:
        raise HTTPException(status_code=400, detail="Email já cadastrado.")
    return cliente_service.criar_novo_cliente(db=db, cliente=cliente)

# 2. Rota para Adicionar Bolo ao Carrinho
@router.post("/carrinho/adicionar/")
def adicionar_ao_carrinho(item: schemas.CarrinhoItemCreate, db: Session = Depends(get_db)):
    sucesso = carrinho_service.adicionar_item(db=db, item=item)
    if not sucesso:
        raise HTTPException(status_code=400, detail="Não foi possível adicionar o item.")
    return {"message": "Item adicionado ao carrinho com sucesso!"}

# 3. Rota para Finalizar o Pedido (Checkout)
@router.post("/checkout/{cliente_id}/")
def finalizar_pedido(cliente_id: int, db: Session = Depends(get_db)):
    pedido = checkout_service.processar_checkout(db=db, cliente_id=cliente_id)
    if not pedido:
        raise HTTPException(status_code=400, detail="Carrinho vazio ou cliente inválido.")
    return {"message": "Pedido realizado!", "pedido_id": pedido.id}