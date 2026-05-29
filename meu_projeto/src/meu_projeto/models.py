from sqlalchemy import Column, Integer, String, ForeignKey
from .models import Cliente, Carrinho, Pedido

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    email = Column(String(100), unique=True)
    telefone = Column(String(20))
    senha = Column(String(100))


class Carrinho(Base):
    __tablename__ = "carrinho"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    produto = Column(String(100))
    quantidade = Column(Integer)


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    produto = Column(String(100))
    quantidade = Column(Integer)
    status = Column(String(50))