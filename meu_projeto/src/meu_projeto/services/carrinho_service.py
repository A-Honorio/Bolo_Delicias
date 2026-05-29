from ..models import carrinho

class CarrinhoService:

    def adicionar(self, db, cliente_id, produto, quantidade):
        item = Carrinho(
            cliente_id=cliente_id,
            produto=produto,
            quantidade=quantidade
        )

        db.add(item)
        db.commit()

        return {"mensagem": "Item adicionado ao carrinho"}

    def listar(self, db, cliente_id):
        return db.query(Carrinho).filter(Carrinho.cliente_id == cliente_id).all()