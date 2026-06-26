from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Text
from sqlalchemy.orm import relationship
from database import Base

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


class FinalizarCompra(Base):
    __tablename__ = 'finalizacoes_compras'

    id = Column(Integer, primary_key=True)
    pedido_id = Column(Integer, ForeignKey('pedidos.id'), nullable=False)
    forma_pagamento = Column(String(50), nullable=False)
    status_pagamento = Column(String(30), default='Pendente')
    endereco_entrega = Column(Text, nullable=False)
    ponto_referencia = Column(String(150))
    data_finalizacao = Column(DateTime, default=datetime.utcnow)

    pedido = relationship('Pedido', backref=relationship('finalizacao', uselist=False))

    def to_dict(self):
        return {
            "id": self.id,
            "pedido_id": self.pedido_id,
            "forma_pagamento": self.forma_pagamento,
            "status_pagamento": self.status_pagamento,
            "endereco_entrega": self.endereco_entrega,
            "data_finalizacao": self.data_finalizacao.strftime('%d/%m/%Y %H:%M:%S') if self.data_finalizacao else None
        }


class AcompanharPedido(Base):
    __tablename__ = 'acompanhamento_pedidos'

    id = Column(Integer, primary_key=True)
    pedido_id = Column(Integer, ForeignKey('pedidos.id'), nullable=False)
    status_atual = Column(String(50), nullable=False, default='Recebido')
    observacao = Column(String(255))
    ultima_atualizacao = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    pedido = relationship('Pedido', backref=relationship('acompanhamentos', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "pedido_id": self.pedido_id,
            "status_atual": self.status_atual,
            "observacao": self.observacao,
            "ultima_atualizacao": self.ultima_atualizacao.strftime('%d/%m/%Y %H:%M:%S') if self.ultima_atualizacao else None
        }