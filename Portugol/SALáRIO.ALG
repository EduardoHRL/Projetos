Algoritmo "Salário_Total"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Marcio Carmona
// Descrição   : o programa calcula o salario total de um vendedor sobre suas vendas
// Autor(a)    : Eduardo
// Data atual  : 19/05/2023
Var
// Seção de Declarações das variáveis 
 SF, TV, P, ST, AD : REAL

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   Escreva ("Digite o Salário Fixo: ")
   Leia(SF)
   Escreva ("Digite o total de vendas em reais:")
   Leia(TV)
   Escreva ("Digite o percentual de vendas (0 a 100) :")
   Leia (P)
   AD := TV*(P/100)
   ST := SF+AD
   Escreva(" O Salário Total é:",ST)
   
Fimalgoritmo