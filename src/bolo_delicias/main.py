from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, SessionLocal, Base
from .views import router as views_router
from .schemas import ClienteCreate as ClienteSchema, CarrinhoItemCreate as CarrinhoSchema
from .services.cliente_service import ClienteService
from .services.carrinho_service import CarrinhoService
from .services.pedido_service import PedidoService

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bolo Delícias API 🍰")

# Instancia os serviços
cliente_service = ClienteService()
carrinho_service = CarrinhoService()
pedido_service = PedidoService()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"mensagem": "Bolo Delicias API 🍰"}


# CLIENTE
@app.post("/clientes")
def cadastrar(cliente: ClienteSchema, db: Session = Depends(get_db)):
    return cliente_service.cadastrar(db, cliente.nome, cliente.email, cliente.telefone, cliente.senha)


# CARRINHO
@app.post("/carrinho")
def adicionar(item: CarrinhoSchema, db: Session = Depends(get_db)):
    return carrinho_service.adicionar(db, item.cliente_id, item.produto, item.quantidade)


@app.get("/carrinho/{cliente_id}")
def ver_carrinho(cliente_id: int, db: Session = Depends(get_db)):
    return carrinho_service.listar(db, cliente_id)


# FINALIZAR
@app.post("/finalizar/{cliente_id}")
def finalizar(cliente_id: int, db: Session = Depends(get_db)):
    return pedido_service.finalizar(db, cliente_id)


# PEDIDOS
@app.get("/pedidos/{cliente_id}")
def listar(cliente_id: int, db: Session = Depends(get_db)):
    return pedido_service.listar(db, cliente_id)


@app.put("/pedidos/{pedido_id}")
def atualizar(pedido_id: int, status: str, db: Session = Depends(get_db)):
    return pedido_service.atualizar_status(db, pedido_id, status)


# VIEWS
app.include_router(views_router)