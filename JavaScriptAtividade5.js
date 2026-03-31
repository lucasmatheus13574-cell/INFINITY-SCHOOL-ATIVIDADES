let tarefas = [];

while (true) {

    let opcao = prompt(
        "=== MENU DE TAREFAS ===\n" +
        "1 - Adicionar tarefa\n" +
        "2 - Listar tarefas\n" +
        "3 - Remover tarefa\n" +
        "4 - Concluir tarefa\n" +
        "5 - Sair\n" +
        "Escolha uma opção:"
    );

    switch (opcao) {


        case "1": 
            let tarefa = prompt("Digite o nome da tarefa:");

            if (tarefa && tarefa.trim() !== "") {
                tarefas.push(tarefa);
                alert("✅ Tarefa adicionada com sucesso!");
            } else {
                alert("⚠️ Tarefa inválida!");
            }
            break;


        case "2":
            if (tarefas.length === 0) {
                alert("📭 Nenhuma tarefa cadastrada.");
            } else {
                let mensagem = "📋 LISTA DE TAREFAS:\n\n";

                let i = 0;
                for (let t of tarefas) {
                    mensagem += `${i} - ${t}\n`;
                    i++;
                }

                alert(mensagem);
            }
            break;


        case "3": 
            if (tarefas.length === 0) {
                alert("⚠️ Lista vazia.");
                break;
            }

            let indiceRemover = prompt("Digite o índice da tarefa que deseja remover:");

            if (indiceRemover >= 0 && indiceRemover < tarefas.length) {
                let removida = tarefas[indiceRemover];
                tarefas.splice(indiceRemover, 1);
                alert(`🗑️ Tarefa "${removida}" removida!`);
            } else {
                alert("❌ Índice inválido!");
            }
            break;

        
        case "4": 
            if (tarefas.length === 0) {
                alert("⚠️ Lista vazia.");
                break;
            }

            let indiceConcluir = prompt("Digite o índice da tarefa concluída:");

            if (indiceConcluir >= 0 && indiceConcluir < tarefas.length) {

                if (!tarefas[indiceConcluir].startsWith("✅ ")) {
                    tarefas[indiceConcluir] = "✅ " + tarefas[indiceConcluir];
                    alert("✔️ Tarefa marcada como concluída!");
                } else {
                    alert("⚠️ Essa tarefa já está concluída.");
                }

            } else {
                alert("❌ Índice inválido!");
            }
            break;

        
        case "5": 
            alert("👋 Encerrando o programa...");
            break;


        default:
            alert("❌ Opção inválida!");
    }

    if (opcao === "5") {
        break;
    }
}