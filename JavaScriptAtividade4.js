let lista = [];

while (true) {
    let opcao = prompt(
        "=== LISTA DE COMPRAS ===\n" +
        "1 - Adicionar item\n" +
        "2 - Remover item\n" +
        "3 - Exibir lista\n" +
        "4 - Atualizar item\n" +
        "5 - Sair\n" +
        "Escolha uma opção:"
    );

    switch (opcao) {

        case "1": 
            let item = prompt("Digite o nome do item:");
            if (item) {
                lista.push(item);
                alert("Item adicionado com sucesso!");
            }
            break;

        case "2": 
            if (lista.length === 0) {
                alert("A lista está vazia!");
                break;
            }

            let removerIndex = prompt("Digite o índice do item que deseja remover:");
            if (removerIndex >= 0 && removerIndex < lista.length) {
                lista.splice(removerIndex, 1);
                alert("Item removido com sucesso!");
            } else {
                alert("Índice inválido!");
            }
            break;

        case "3": 
            if (lista.length === 0) {
                alert("A lista está vazia!");
            } else {
                let mensagem = "=== SUA LISTA ===\n";

                let index = 0;
                for (let item of lista) {
                    mensagem += index + " - " + item + "\n";
                    index++;
                }

                alert(mensagem);
            }
            break;

        case "4": 
            if (lista.length === 0) {
                alert("A lista está vazia!");
                break;
            }

            let atualizarIndex = prompt("Digite o índice do item que deseja atualizar:");
            if (atualizarIndex >= 0 && atualizarIndex < lista.length) {
                let novoValor = prompt("Digite o novo valor:");
                lista[atualizarIndex] = novoValor;
                alert("Item atualizado com sucesso!");
            } else {
                alert("Índice inválido!");
            }
            break;

        case "5": 
            alert("Encerrando o programa...");
            break;

        default:
            alert("Opção inválida!");
    }

    if (opcao === "5") {
        break;
    }
}