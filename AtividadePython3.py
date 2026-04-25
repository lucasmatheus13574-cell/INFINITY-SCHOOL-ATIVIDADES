produtos = {}


for i in range(5):
    nome = input(f"Digite o nome do {i+1}º produto: ")
    preco = float(input(f"Digite o preço do {i+1}º produto: R$ "))
    

    produtos[nome] = preco


total = sum(produtos.values())


print("\nProdutos cadastrados:", produtos)
print(f"Valor total da compra: R$ {total:.2f}")