tarefas = []


def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    prioridade = input("Digite a prioridade (baixa, média, alta): ")
    categoria = input("Digite a categoria da tarefa: ")

    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }

    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!\n")



def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.\n")
        return

    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"

        print(f"""
Tarefa {i}
Nome: {tarefa['nome']}
Descrição: {tarefa['descricao']}
Prioridade: {tarefa['prioridade']}
Categoria: {tarefa['categoria']}
Status: {status}
""")



def concluir_tarefa():
    listar_tarefas()

    if tarefas:
        numero = int(input("Digite o número da tarefa que deseja concluir: "))

        if 1 <= numero <= len(tarefas):
            tarefas[numero - 1]["concluida"] = True
            print("Tarefa marcada como concluída!\n")
        else:
            print("Número inválido.\n")



def filtrar_prioridade():
    prioridade = input("Digite a prioridade para filtrar: ")

    print(f"\nTarefas com prioridade '{prioridade}':")
    for tarefa in tarefas:
        if tarefa["prioridade"].lower() == prioridade.lower():
            print(f"- {tarefa['nome']}")



def filtrar_categoria():
    categoria = input("Digite a categoria para filtrar: ")

    print(f"\nTarefas da categoria '{categoria}':")
    for tarefa in tarefas:
        if tarefa["categoria"].lower() == categoria.lower():
            print(f"- {tarefa['nome']}")



def menu():
    while True:
        print("""
===== GERENCIADOR DE TAREFAS =====

1 - Adicionar tarefa
2 - Listar tarefas
3 - Concluir tarefa
4 - Filtrar por prioridade
5 - Filtrar por categoria
6 - Sair

==================================
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            concluir_tarefa()

        elif opcao == "4":
            filtrar_prioridade()

        elif opcao == "5":
            filtrar_categoria()

        elif opcao == "6":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida!\n")



menu()