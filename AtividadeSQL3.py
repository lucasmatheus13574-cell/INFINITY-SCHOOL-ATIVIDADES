CREATE TABLE Estoque (
    EstoqueID INT PRIMARY KEY,
    ProdutoID INT,
    FornecedorID INT,
    Quantidade INT NOT NULL,
    DataEntrada DATE NOT NULL,
    
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID),
    FOREIGN KEY (FornecedorID) REFERENCES Fornecedores(FornecedorID)
);