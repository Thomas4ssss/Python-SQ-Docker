CREATE DATABASE Livros;
USE Livros;

CREATE TABLE projeto(
    id int not null auto_increment, 
    nome_livro text not null,
    autor_livro text not null,
    ano int,
    paginas int,
    entregar_dia DATE not null
);

INSERT INTO projeto(nome_livro, autor_livro, ano, paginas, entregar_dia)
VALUES("0","0","0","0","2023-07-11");
