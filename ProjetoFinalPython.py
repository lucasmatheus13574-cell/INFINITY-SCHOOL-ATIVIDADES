import mysql.connector
from datetime import date



conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="LojaEstoque"
)

cursor = conexao.cursor()





class Produto:
    def __init__(self, nome, descricao, quantidade, preco):
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco


class Venda:
    def __init__(self, id_produto, quantidade_vendida):
        self.id_produto = id_produto
        self.quantidade_vendida = quantidade_vendida
        self.data_venda = date.today()




def cadastrar_produto():
    nome = input("Nome do produto: ")
    descricao = input("Descrição: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))

    produto = Produto(nome, descricao, quantidade, preco)

    sql = "INSERT INTO Produtos (Nome, Descricao, Quantidade, Preco) VALUES (%s, %s, %s, %s)"
    valores = (produto.nome, produto.descricao, produto.quantidade, produto.preco)

    cursor.execute(sql, valores)
    conexao.commit()

    print("Produto cadastrado com sucesso!\n")




def listar_produtos():
    cursor.execute("SELECT * FROM Produtos")
    resultados = cursor.fetchall()

    print("\n--- LISTA DE PRODUTOS ---")
    for produto in resultados:
        print(f"ID: {produto[0]} | Nome: {produto[1]} | Descrição: {produto[2]} | Quantidade: {produto[3]} | Preço: R$ {produto[4]:.2f}")
    print()




def atualizar_quantidade():
    id_produto = int(input("Digite o ID do produto: "))
    nova_quantidade = int(input("Nova quantidade: "))

    sql = "UPDATE Produtos SET Quantidade = %s WHERE ID = %s"
    valores = (nova_quantidade, id_produto)

    cursor.execute(sql, valores)
    conexao.commit()

    print("Quantidade atualizada com sucesso!\n")




def remover_produto():
    id_produto = int(input("Digite o ID do produto para remover: "))

    sql = "DELETE FROM Produtos WHERE ID = %s"
    valores = (id_produto,)

    cursor.execute(sql, valores)
    conexao.commit()

    print("Produto removido com sucesso!\n")





def registrar_venda():
    id_produto = int(input("ID do produto vendido: "))
    quantidade_vendida = int(input("Quantidade vendida: "))

    venda = Venda(id_produto, quantidade_vendida)

    sql_venda = "INSERT INTO Vendas (IDProduto, QuantidadeVendida, DataVenda) VALUES (%s, %s, %s)"
    valores_venda = (venda.id_produto, venda.quantidade_vendida, venda.data_venda)

    cursor.execute(sql_venda, valores_venda)

    sql_estoque = "UPDATE Produtos SET Quantidade = Quantidade - %s WHERE ID = %s"
    valores_estoque = (quantidade_vendida, id_produto)

    cursor.execute(sql_estoque, valores_estoque)
    conexao.commit()

    print("Venda registrada com sucesso!\n")




while True:
    print("=== SISTEMA DE GERENCIAMENTO DE ESTOQUE ===")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Atualizar Quantidade")
    print("4 - Remover Produto")
    print("5 - Registrar Venda")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        atualizar_quantidade()
    elif opcao == "4":
        remover_produto()
    elif opcao == "5":
        registrar_venda()
    elif opcao == "0":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida!\n")


cursor.close()
conexao.close()
