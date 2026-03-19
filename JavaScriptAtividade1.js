let num1 = Number(prompt("Digite o primeiro número:"));
let num2 = Number(prompt("Digite o segundo número:"));

let soma = num1 + num2;
let subtracao = num1 - num2;
let multiplicacao = num1 * num2;
let divisao = num1 / num2;
let resto = num1 % num2;


console.log("Soma:", soma);
console.log("Subtração:", subtracao);
console.log("Multiplicação:", multiplicacao);
console.log("Divisão:", divisao);
console.log("Resto da divisão:", resto);


let resultado = num1;

resultado += num2; 
console.log("Usando += :", resultado);

resultado -= num2; 
console.log("Usando -= :", resultado);

resultado *= num2; 
console.log("Usando *= :", resultado);

resultado /= num2; 
console.log("Usando /= :", resultado);

resultado %= num2; 
console.log("Usando %= :", resultado);