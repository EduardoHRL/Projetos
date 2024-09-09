Algoritmo "Maior_Deles"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 19/05/2023
Var
// Seção de Declarações das variáveis 
N1,N2, N3 : REAL

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   Escreva ("Digite um numero:")
   Leia(N1)
   Escreva ("Digite OUTRO numero:")
   Leia(N2)
   Escreva ("Digite OUTRO numero:")
   Leia(N3)
   SE (N1>N2) e( N1>N3) ENTAO
      Escreva(" o primeiro numero é maior")
   Fimse
   Se (N2>N1) e (N2>N3) Entao
      Escreva ("o segundo numero é o maior")
   Fimse
   Se (N3>N1) e (N3>N2) Entao
      Escreva ("o terceiro numero é o maior")
   Fimse
Fimalgoritmo