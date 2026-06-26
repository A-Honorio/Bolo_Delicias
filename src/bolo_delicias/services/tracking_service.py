from database import db
from models.acompanhar_pedido import AcompanharPedido

class AcompanharPedidoService:

    @staticmethod
    def obter_status_atual(pedido_id):
        """
        Retorna o histórico e o status atual do pedido do cliente.
        """
        historico = AcompanharPedido.query.filter_by(pedido_id=pedido_id).order_by(AcompanharPedido.ultima_atualizacao.desc()).all()
        
        if not historico:
            return {"erro": "Nenhum histórico encontrado para este pedido."}, 404
            
        return [registro.to_dict() for registro in historico], 200

    @staticmethod
    def atualizar_status_confeitaria(pedido_id, novo_status, observacao=None):
        """
        Método usado pelo admin/confeiteiro para mudar o status (Ex: 'Na Cozinha' -> 'Pronto para Entrega')
        """
        status_permitidos = ['Recebido', 'Na Cozinha', 'Pronto para Entrega', 'Saiu para Entrega', 'Entregue']
        
        if novo_status not in status_permitidos:
            return {"erro": "Status inválido."}, 400

        novo_registro = AcompanharPedido(
            pedido_id=pedido_id,
            status_atual=novo_status,
            observacao=observacao
        )

        try:
            db.session.add(novo_registro)
            db.session.commit()
            return {"mensagem": f"Status atualizado para: {novo_status}"}, 200
        except Exception as e:
            db.session.rollback()
            return {"erro": f"Erro ao atualizar status: {str(e)}"}, 500