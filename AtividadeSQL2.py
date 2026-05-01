CREATE TABLE Produtos (
    ProdutoID INT PRIMARY KEY,
    NomeProduto VARCHAR(100) NOT NULL,
    Quantidade INT NOT NULL,
    Preco DECIMAL(10,2) NOT NULL
);

INSERT INTO Produtos (ProdutoID, NomeProduto, Quantidade, Preco)
VALUES
(1, 'Notebook', 10, 3500.00),
(2, 'Mouse', 50, 80.00),
(3, 'Teclado', 30, 150.00);