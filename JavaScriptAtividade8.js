const aluno = {
    nome: "Lucas",
    notas: [7, 8, 9],

    calcularMedia() {
        const soma = this.notas.reduce((acc, nota) => acc + nota, 0);
        return soma / this.notas.length;
    }
};

// nome: string com o nome do aluno
// notas: array de números
// calcularMedia(): método que usa reduce() para somar as notas e dividir pela quantidade de notas, retornando a média.