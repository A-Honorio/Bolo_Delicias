from database import db
from models.finalizar_compra import FinalizarCompra
from models.acompanhar_pedido import AcompanharPedido

class FinalizarCompraService:
    
    @staticmethod
    def processar_checkout(pedido_id, dados_pagamento):
        """
        Gera o registro de finalização de compra e inicia o rastreio do pedido.
        """

        if not dados_pagamento.get('endereco_entrega') or not dados_pagamento.get('forma_pagamento'):
            return {"erro": "Endereço e forma de pagamento são obrigatórios"}, 400

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
            db.session.add(nova_finalizacao)
            db.session.add(primeiro_passo)
            db.session.commit()
            return {"mensagem": "Compra finalizada com sucesso!", "dados": nova_finalizacao.to_dict()}, 201
        except Exception as e:
            db.session.rollback()
            return {"erro": f"Erro ao finalizar compra: {str(e)}"}, 500