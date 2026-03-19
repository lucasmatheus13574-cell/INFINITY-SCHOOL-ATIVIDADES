
let idade = Number(prompt("Digite sua idade:"));
let status = prompt("Digite seu status (registrado ou não registrado):").toLowerCase();


let maioridade = (idade >= 18) ? "Maior de idade" : "Menor de idade";
console.log(maioridade);


switch (status) {
    case "registrado":
        console.log("Bem-vindo! Você está registrado.");
        break;

    case "não registrado":
        console.log("Por favor, complete seu registro.");
        break;

    default:
        console.log("Status desconhecido.");
}


if (idade >= 18 && status === "registrado") {
    console.log("Acesso completo liberado.");
} else if (idade < 18 || status !== "registrado") {
    console.log("Acesso limitado.");
}