Algoritmo "Votação"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 19/05/2023
Var
// Seção de Declarações das variáveis 
TE, VB, VN, VV, PV, PN, PB  : Real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   Escreva (" Digite a quntidade total de eleitores:")
   Leia(TE)
   Escreva (" Digite a quantidade de votos validos:")
   Leia(VV)
   Escreva (" Digite a quantidade de votos brancos:")
   Leia(VB)
   Escreva (" Digite a quantidade de votos nulos:")
   Leia(VN)
   PV := ((VV/TE)*100)
   Escreva (" A porcentagem de Votos validos em relação ao total de eleitores é:", PV)
   PN := ((VN/TE)*100)
   Escreva (" A porcentagem de Votos Nulos em relação ao total de eleitores é:", PN)
   PB := ((VB/TE)*100)
   Escreva (" A porcentagem de Votos Brancos em relação ao total de eleitores é:", PB)
Fimalgoritmo