-- ===================================================
-- BANCO DE DADOS BOLO_DELICIAS
-- ===================================================

DROP DATABASE IF EXISTS bolo_delicias;

CREATE DATABASE bolo_delicias;

USE bolo_delicias;

-- ===================================================
-- CLIENTES
-- ===================================================

CREATE TABLE clientes (

    id INT AUTO_INCREMENT PRIMARY KEY,

    nome VARCHAR(100) NOT NULL,

    email VARCHAR(100) NOT NULL UNIQUE,

    telefone VARCHAR(20),

    senha VARCHAR(100) NOT NULL

);

-- ===================================================
-- CARRINHO
-- ===================================================

CREATE TABLE carrinho (

    id INT AUTO_INCREMENT PRIMARY KEY,

    cliente_id INT NOT NULL,

    produto VARCHAR(100) NOT NULL,

    quantidade INT NOT NULL,

    CONSTRAINT fk_carrinho_cliente
        FOREIGN KEY (cliente_id)
        REFERENCES clientes(id)
        ON DELETE CASCADE

);

-- ===================================================
-- PEDIDOS
-- ===================================================

CREATE TABLE pedidos (

    id INT AUTO_INCREMENT PRIMARY KEY,

    cliente_id INT NOT NULL,

    produto VARCHAR(100) NOT NULL,

    quantidade INT NOT NULL,

    status VARCHAR(50),

    CONSTRAINT fk_pedido_cliente
        FOREIGN KEY (cliente_id)
        REFERENCES clientes(id)
        ON DELETE CASCADE

);

-- ===================================================
-- FINALIZAÇÃO DA COMPRA
-- ===================================================

CREATE TABLE finalizacoes_compras (

    id INT AUTO_INCREMENT PRIMARY KEY,

    pedido_id INT NOT NULL UNIQUE,

    forma_pagamento VARCHAR(50) NOT NULL,

    status_pagamento VARCHAR(30) DEFAULT 'Pendente',

    endereco_entrega TEXT NOT NULL,

    ponto_referencia VARCHAR(150),

    data_finalizacao DATETIME DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_finalizacao_pedido
        FOREIGN KEY (pedido_id)
        REFERENCES pedidos(id)
        ON DELETE CASCADE

);

-- ===================================================
-- ACOMPANHAMENTO DO PEDIDO
-- ===================================================

CREATE TABLE acompanhamento_pedidos (

    id INT AUTO_INCREMENT PRIMARY KEY,

    pedido_id INT NOT NULL,

    status_atual VARCHAR(50) DEFAULT 'Recebido',

    observacao VARCHAR(255),

    ultima_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_acompanhamento_pedido
        FOREIGN KEY (pedido_id)
        REFERENCES pedidos(id)
        ON DELETE CASCADE

);