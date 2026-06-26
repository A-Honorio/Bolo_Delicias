from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

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

class FinalizarCompra(db.Model):
    __tablename__ = 'finalizacoes_compras'

    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False)
    forma_pagamento = db.Column(db.String(50), nullable=False)
    status_pagamento = db.Column(db.String(30), default='Pendente')
    endereco_entrega = db.Column(db.Text, nullable=False)
    ponto_referencia = db.Column(db.String(150))
    data_finalizacao = db.Column(db.DateTime, default=datetime.utcnow)

    pedido = db.relationship('Pedido', backref=db.backref('finalizacao', uselist=False))

    def to_dict(self):
        return {
            "id": self.id,
            "pedido_id": self.pedido_id,
            "forma_pagamento": self.forma_pagamento,
            "status_pagamento": self.status_pagamento,
            "endereco_entrega": self.endereco_entrega,
            "data_finalizacao": self.data_finalizacao.strftime('%d/%m/%Y %H:%M:%S')
        }
    
class AcompanharPedido(db.Model):
    __tablename__ = 'acompanhamento_pedidos'

    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False)
    status_atual = db.Column(db.String(50), nullable=False, default='Recebido')
    observacao = db.Column(db.String(255))
    ultima_atualizacao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    pedido = db.relationship('Pedido', backref=db.backref('acompanhamentos', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "pedido_id": self.pedido_id,
            "status_atual": self.status_atual,
            "observacao": self.observacao,
            "ultima_atualizacao": self.ultima_atualizacao.strftime('%d/%m/%Y %H:%M:%S')
        }