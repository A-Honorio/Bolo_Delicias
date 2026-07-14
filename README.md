# 🍰 Bolo Delícias

Sistema desenvolvido para a disciplina de Programação com Acesso a Banco de Dados.

## Tecnologias

- Python
- FastAPI
- SQLAlchemy
- MySQL
- Poetry

## Como executar

### 1. Clone o projeto

```bash
git clone https://github.com/A-Honorio/Bolo_Delicias.git
```

### 2. Entre na pasta

```bash
cd Bolo_Delicias
```

### 3. Instale as dependências

```bash
poetry install
```

### 4. Configure o banco

Crie um arquivo `.env` utilizando o modelo do `.env.example`.

### 5. Execute o script SQL

Abra o MySQL Workbench e execute:

```sql
SOURCE schema.sql;
```

ou importe o arquivo `schema.sql`.

### 6. Rode a aplicação

```bash
poetry run uvicorn main:app --reload
```

### 7. Acesse

```
http://127.0.0.1:8000/docs
```