from models import Cliente 

class ClienteService:

    def cadastrar(self, db, nome, email, telefone, senha):
        existente = db.query(Cliente).filter(Cliente.email == email).first()

        if existente:
            return {"erro": "Email já cadastrado"}

        novo = Cliente(
            nome=nome,
            email=email,
            telefone=telefone,
            senha=senha
        )

        db.add(novo)
        db.commit()

        return {"mensagem": "Cliente cadastrado com sucesso"}