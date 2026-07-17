from sqlalchemy.orm import Session
from ..models import FinalizarCompra, AcompanharPedido

class FinalizarCompraService:
    
    @staticmethod
    def processar_checkout(db: Session, pedido_id: int, dados_pagamento: dict):
        """
        Gera o registro de finalização de compra e inicia o rastreio do pedido.
        """

        if not dados_pagamento.get('endereco_entrega') or not dados_pagamento.get('forma_pagamento'):
            return {"erro": "Endereço e forma de pagamento são obrigatórios"}

        nova_finalizacao = FinalizarCompra(
            pedido_id=pedido_id,
            forma_pagamento=dados_pagamento['forma_pagamento'],
            endereco_entrega=dados_pagamento['endereco_entrega'],
            ponto_referencia=dados_pagamento.get('ponto_referencia', ''),
            status_pagamento='Aprovado'
        )

        primeiro_passo = AcompanharPedido(
            pedido_id=pedido_id,
            status_atual='Recebido',
            observacao='Seu pedido de bolo foi recebido pela nossa confeitaria!'
        )

        try:
            db.add(nova_finalizacao)
            db.add(primeiro_passo)
            db.commit()
            
            db.refresh(nova_finalizacao)
            
            return {"mensagem": "Compra finalizada com sucesso!", "dados": nova_finalizacao.to_dict()}
        except Exception as e:
            db.rollback()
            return {"erro": f"Erro ao finalizar compra: {str(e)}"}