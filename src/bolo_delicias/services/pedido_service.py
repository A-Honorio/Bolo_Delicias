from models import Pedido, Carrinho

class PedidoService:

    def finalizar(self, db, cliente_id):
        itens = db.query(Carrinho).filter(Carrinho.cliente_id == cliente_id).all()

        if not itens:
            return {"erro": "Carrinho vazio"}

        for item in itens:
            pedido = Pedido(
                cliente_id=cliente_id,
                produto=item.produto,
                quantidade=item.quantidade,
                status="Em preparo"
            )
            db.add(pedido)

        db.query(Carrinho).filter(Carrinho.cliente_id == cliente_id).delete()

        db.commit()

        return {"mensagem": "Pedido finalizado"}

    def listar(self, db, cliente_id):
        return db.query(Pedido).filter(Pedido.cliente_id == cliente_id).all()

    def atualizar_status(self, db, pedido_id, status):
        pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()

        if not pedido:
            return {"erro": "Pedido não encontrado"}

        pedido.status = status
        db.commit()
        db.refresh(pedido)

        return {"mensagem": "Status atualizado"}