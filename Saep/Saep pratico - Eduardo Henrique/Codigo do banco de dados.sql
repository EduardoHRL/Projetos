CREATE DATABASE db_saep1;
USE db_saep1;

CREATE TABLE tbl_usuario (
	usu_id INT PRIMARY KEY AUTO_INCREMENT,
    usu_nome VARCHAR(255),
    usu_email VARCHAR(255)
);

CREATE TABLE tbl_tarefas (
	tar_id INT PRIMARY KEY AUTO_INCREMENT,
    usu_id INT,
    tar_descricao VARCHAR(255),
    tar_nomeSetor VARCHAR(45),
    tar_prioridade VARCHAR(45),
    tar_data DATE,
    tar_status VARCHAR(45) default 'A fazer',
    FOREIGN KEY (usu_id) REFERENCES tbl_usuario(usu_id) ON DELETE CASCADE
)