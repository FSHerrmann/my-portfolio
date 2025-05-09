let nomeFuncionario;
let horasTrabalhadas;
let valorHora;
let salarioMensal;
let limiteHorasNormais = 220; // Limite de horas normais
let setorFuncionario; // Defina o setor do funcionário (ex: "AD", "GE", "OP")

// Função para alterar o valor do salário base de acordo com o setor
function alterarSalarioBase(setor) {
    if (setor === "AD") {
        valorHora = valorHora * 1.1; // 10% a mais para o setor Administrativo
    } else if (setor === "GE") {
        valorHora = valorHora * 1.25; // 25% a mais para o setor Gerência
    }
    // O setor Operacional (OP) não altera o valor da hora, então não é necessário
}

// Função para calcular o salário mensal (com ou sem horas extras, dependendo do setor)
function calcularSalario() {
    if (setorFuncionario === "GE") {
        // Gerência não tem horas extras
        salarioMensal = horasTrabalhadas * valorHora;
    } else {
        // Para os setores Operacional e Administrativo, calculamos as horas extras
        if (horasTrabalhadas > limiteHorasNormais) {
            let horasExtras = horasTrabalhadas - limiteHorasNormais;
            salarioMensal = (limiteHorasNormais * valorHora) + (horasExtras * valorHora * 2); // Horas extras são dobradas
        } else {
            salarioMensal = horasTrabalhadas * valorHora; // Caso não haja horas extras
        }
    }
}

// Exemplo de uso:

// Definir valor hora, nome do funcionário, horas trabalhadas e setor
nomeFuncionario = "João";
horasTrabalhadas = 230; // Exemplo de horas trabalhadas
valorHora = 20; // Exemplo de valor hora
setorFuncionario = "AD"; // Exemplo de setor (pode ser "AD", "GE" ou "OP")

// Alterando o salário base de acordo com o setor
alterarSalarioBase(setorFuncionario);

// Calculando o salário mensal
calcularSalario();

// Exibindo o salário final
console.log(`O salário de ${nomeFuncionario} é R$${salarioMensal.toFixed(2)}`);
