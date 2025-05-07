CREATE DATABASE Produtos
USE Produtos
CREATE TABLE  IF NOT EXISTS Produtos (
	ProdutoID INT PRIMARY KEY AUTO_INCREMENT,
    NomeProduto VARCHAR(100) NOT NULL,
    Quantidade INT NOT NULL,
    Preco FLOAT NOT NULL
);

INSERT INTO Produtos (NomeProduto, Quantidade, Preco) 
VALUES ("Notebook Lenovo i3", 10, 2500)

INSERT INTO Produtos (NomeProduto, Quantidade, Preco) 
VALUES ("Mouse Logitech g450", 12, 350)

INSERT INTO Produtos (NomeProduto, Quantidade, Preco) 
VALUES ("Processador Ryzen 5500", 5, 670)

SELECT * FROM Produtos