from sqlalchemy.orm import Session
from models import AcompanharPedido

class AcompanharPedidoService:

    @staticmethod
    def obter_status_atual(db: Session, pedido_id: int):
        """
        Retorna o histórico e o status atual do pedido do cliente.
        """
        historico = (
            db.query(AcompanharPedido)
            .filter(AcompanharPedido.pedido_id == pedido_id)
            .order_by(AcompanharPedido.ultima_atualizacao.desc())
            .all()
        )
        
        if not historico:
            return {"erro": "Nenhum histórico encontrado para este pedido."}
            
        return [registro.to_dict() for registro in historico]

    @staticmethod
    def atualizar_status_confeitaria(db: Session, pedido_id: int, novo_status: str, observacao: str = None):
        """
        Método usado pelo admin/confeiteiro para mudar o status (Ex: 'Na Cozinha' -> 'Pronto para Entrega')
        """
        status_permitidos = ['Recebido', 'Na Cozinha', 'Pronto para Entrega', 'Saiu para Entrega', 'Entregue']
        
        if novo_status not in status_permitidos:
            return {"erro": "Status inválido."}

        novo_registro = AcompanharPedido(
            pedido_id=pedido_id,
            status_atual=novo_status,
            observacao=observacao
        )

        try:
            db.add(novo_registro)
            db.commit()
            return {"mensagem": f"Status atualizado para: {novo_status}"}
        except Exception as e:
            db.rollback()
            return {"erro": f"Erro ao atualizar status: {str(e)}"}