let tarefas = [];


const adicionarTarefa = function (nome) {
    tarefas.push({
        descricao: nome,
        concluida: false
    });
    console.log(`Tarefa "${nome}" adicionada com sucesso!`);
};


const listarTarefas = () => {
    if (tarefas.length === 0) {
        console.log("Nenhuma tarefa cadastrada.");
        return;
    }

    console.log("\n=== LISTA DE TAREFAS ===");
    tarefas.forEach((tarefa, indice) => {
        let status = tarefa.concluida ? "✅ Concluída" : "❌ Pendente";
        console.log(`${indice}: ${tarefa.descricao} - ${status}`);
    });
};


function executarOperacao(indice, callback, novoTexto = null) {
    if (indice < 0 || indice >= tarefas.length || isNaN(indice)) {
        console.log("Índice inválido!");
        return;
    }

    callback(indice, novoTexto);
}


function removerTarefa(indice) {
    let removida = tarefas.splice(indice, 1);
    console.log(`Tarefa "${removida[0].descricao}" removida com sucesso!`);
}


function atualizarTarefa(indice, novoTexto) {
    let antiga = tarefas[indice].descricao;
    tarefas[indice].descricao = novoTexto;
    console.log(`Tarefa "${antiga}" atualizada para "${novoTexto}"!`);
}


function concluirTarefa(indice) {
    tarefas[indice].concluida = true;
    console.log(`Tarefa "${tarefas[indice].descricao}" marcada como concluída!`);
}


let opcao;

while (opcao !== "6") {
    opcao = prompt(
        "=== MENU DE TAREFAS ===\n" +
        "1 - Adicionar tarefa\n" +
        "2 - Listar tarefas\n" +
        "3 - Remover tarefa\n" +
        "4 - Atualizar tarefa\n" +
        "5 - Concluir tarefa\n" +
        "6 - Sair\n\n" +
        "Escolha uma opção:"
    );

    switch (opcao) {
        case "1":
            let novaTarefa = prompt("Digite o nome da nova tarefa:");
            if (novaTarefa && novaTarefa.trim() !== "") {
                adicionarTarefa(novaTarefa);
            } else {
                console.log("Nome da tarefa inválido.");
            }
            break;

        case "2":
            listarTarefas();
            break;

        case "3":
            listarTarefas();
            let indiceRemover = parseInt(prompt("Digite o índice da tarefa que deseja remover:"));
            executarOperacao(indiceRemover, removerTarefa);
            break;

        case "4":
            listarTarefas();
            let indiceAtualizar = parseInt(prompt("Digite o índice da tarefa que deseja atualizar:"));
            let novoTexto = prompt("Digite o novo nome da tarefa:");
            if (novoTexto && novoTexto.trim() !== "") {
                executarOperacao(indiceAtualizar, atualizarTarefa, novoTexto);
            } else {
                console.log("Novo texto inválido.");
            }
            break;

        case "5":
            listarTarefas();
            let indiceConcluir = parseInt(prompt("Digite o índice da tarefa que deseja concluir:"));
            executarOperacao(indiceConcluir, concluirTarefa);
            break;

        case "6":
            console.log("Encerrando o programa...");
            break;

        default:
            console.log("Opção inválida! Tente novamente.");
    }
}