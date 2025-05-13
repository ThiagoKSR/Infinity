CREATE DATABASE BancoDados
USE BancoDados

CREATE TABLE IF NOT EXISTS Produtos (
    ProdutoID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100) NOT NULL,
    Descricao TEXT,
    Preco DECIMAL(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS Fornecedores (
    FornecedorID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100) NOT NULL,
    CNPJ VARCHAR(14) UNIQUE
);

CREATE TABLE Estoque (
	EstoqueID INT PRIMARY KEY AUTO_INCREMENT,
    ProdutoID INT NOT NULL,
    FornecedorID INT NOT NULL,
    Quantidade INT NOT NULL,
    DataEntrada DATE NOT NULL,
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID),
    FOREIGN KEY (FornecedorID) REFERENCES Fornecedores(FornecedorID)
);

SELECT e.*, p.Nome AS ProdutoNome, f.Nome AS FornecedorNome
FROM Estoque e
LEFT JOIN Produtos p ON e.ProdutoID = p.ProdutoID
LEFT JOIN Fornecedores f ON e.FornecedorID = f.FornecedorID
UNION

SELECT e.*, p.Nome AS ProdutoNome, f.Nome AS FornecedorNome
FROM Estoque e
RIGHT JOIN Produtos p ON e.ProdutoID = p.ProdutoID
RIGHT JOIN Fornecedores f ON e.FornecedorID = f.FornecedorID
WHERE e.EstoqueID IS NULL;

SELECT 
    p.Nome AS Produto,
    SUM(e.Quantidade) AS TotalEstoque
FROM Estoque e
JOIN Produtos p ON e.ProdutoID = p.ProdutoID
GROUP BY p.Nome;

ALTER TABLE Estoque
ADD COLUMN Localizacao VARCHAR(50) AFTER Quantidade;

ALTER TABLE Estoque
MODIFY COLUMN Quantidade DECIMAL(10,2);