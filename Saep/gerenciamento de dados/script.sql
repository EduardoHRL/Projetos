CREATE DATABASE db_dados;
USE db_dados;

CREATE TABLE clientes(
	id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    email VARCHAR(255),
    telefone VARCHAR(14)
);

CREATE TABLE produtos (
	id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    descricao VARCHAR(255),
    preco FLOAT
);

CREATE TABLE pedidos (
	id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    data_pedido DATE,
    cliente INT,
    produto INT,
	FOREIGN KEY (cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (produto) REFERENCES produtos(id_produto)
)