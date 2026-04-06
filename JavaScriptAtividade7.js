let nomes = [];
let opcao = "";

while (opcao !== "6") {
    opcao = prompt(
        "=== MENU ===\n" +
        "1 - Adicionar nome\n" +
        "2 - Filtrar nomes por letra inicial\n" +
        "3 - Buscar nome específico\n" +
        "4 - Transformar nomes em MAIÚSCULAS\n" +
        "5 - Verificar se todos os nomes têm mais de 3 caracteres\n" +
        "6 - Sair\n\n" +
        "Escolha uma opção:"
    );

    switch (opcao) {
        case "1":
            let novoNome = prompt("Digite um nome para adicionar:");
            if (novoNome && novoNome.trim() !== "") {
                nomes.push(novoNome.trim());
                console.log("Nome adicionado com sucesso!");
                console.log("Lista atualizada:", nomes);
            } else {
                console.log("Nome inválido.");
            }
            break;

        case "2":
            if (nomes.length === 0) {
                console.log("A lista está vazia.");
            } else {
                let letra = prompt("Digite a letra inicial para filtrar os nomes:");
                if (letra && letra.trim() !== "") {
                    let nomesFiltrados = nomes.filter(nome =>
                        nome.toLowerCase().startsWith(letra.toLowerCase())
                    );
                    console.log("Nomes filtrados:", nomesFiltrados);
                } else {
                    console.log("Letra inválida.");
                }
            }
            break;

        case "3":
            if (nomes.length === 0) {
                console.log("A lista está vazia.");
            } else {
                let nomeBusca = prompt("Digite o nome que deseja buscar:");
                let encontrado = nomes.find(nome => nome.toLowerCase() === nomeBusca.toLowerCase());

                if (encontrado) {
                    console.log("Nome encontrado:", encontrado);
                } else {
                    console.log("Nome não encontrado.");
                }
            }
            break;

        case "4":
            if (nomes.length === 0) {
                console.log("A lista está vazia.");
            } else {
                let nomesMaiusculos = nomes.map(nome => nome.toUpperCase());
                console.log("Lista transformada em maiúsculas:", nomesMaiusculos);
            }
            break;

        case "5":
            if (nomes.length === 0) {
                console.log("A lista está vazia.");
            } else {
                let todosMaioresQueTres = nomes.every(nome => nome.length > 3);
                console.log("Todos os nomes têm mais de 3 caracteres?", todosMaioresQueTres);
            }
            break;

        case "6":
            console.log("Programa encerrado.");
            break;

        default:
            console.log("Opção inválida. Tente novamente.");
    }
}