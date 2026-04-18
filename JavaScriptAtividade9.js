const aluno = {
    nome: "Lucas",
    idade: 17,
    notas: [6, 7.5, 8],

    calcularMedia() {
        const soma = this.notas.reduce((acc, nota) => acc + nota, 0);
        return soma / this.notas.length;
    }
};


const { nome, idade } = aluno;


aluno.notas = [...aluno.notas, 9];


function verificarSituacao(media) {
    if (media >= 7) {
        return "Aprovado";
    } else {
        return "Reprovado";
    }
}


console.log("Notas do aluno:");
for (let i = 0; i < aluno.notas.length; i++) {
    console.log(`Nota ${i + 1}: ${aluno.notas[i]}`);
}


const mediaFinal = aluno.calcularMedia();


const situacao = verificarSituacao(mediaFinal);


console.log("\n--- Resultado ---");
console.log(`Nome: ${nome}`);
console.log(`Idade: ${idade}`);
console.log(`Média: ${mediaFinal.toFixed(2)}`);
console.log(`Situação: ${situacao}`);