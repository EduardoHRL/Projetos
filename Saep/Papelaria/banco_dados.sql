CREATE DATABASE db_papelaria;
USE db_papelaria;

CREATE TABLE livros (
	id_livro INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100),
    isbn VARCHAR(17),
    edicao VARCHAR(45),
    editora VARCHAR(100),
    ano_publicacao INT,
    preco FLOAT,
    categoria VARCHAR(45)
);

CREATE TABLE autores (
	id_autor INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    nacionalidade VARCHAR(50),
    biografia LONGTEXT
);

CREATE TABLE livros_autores(
	livro_id INT,
    autor_id INT,
    PRIMARY KEY(livro_id, autor_id),
    FOREIGN KEY(livro_id) REFERENCES livros(id_livro) ON DELETE CASCADE,
    FOREIGN KEY(autor_id) REFERENCES autores(id_autor) ON DELETE CASCADE
);

CREATE TABLE compras(
	id_compra INT PRIMARY KEY AUTO_iNCREMENT,
    livro_comprado INT,
    quantidade INT,
    data_compra DATETIME,
    FOREIGN KEY(livro_comprado) REFERENCES livros(id_livro) ON DELETE CASCADE
);

CREATE TABLE vendas(
	id_venda INT PRIMARY KEY AUTO_INCREMENT,
    livro_vendido INT,
    quantidade INT,
    data_venda DATETIME,
    FOREIGN KEY(livro_vendido) REFERENCES livros(id_livro) ON DELETE CASCADE
);





