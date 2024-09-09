Algoritmo "Peças_e_PREÇO"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 19/05/2023
Var
// Seção de Declarações das variáveis 
IPI, VU1, QP1, P2, VU2, QP2, VT   : REAL

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   Escreva("Digite o valor da peça 1:")
   Leia(VU1)
   Escreva("Digite a quantidade de peças 1:")
   Leia(QP1)
   Escreva("Digite o valor da peça 2:")
   Leia(VU2)
   Escreva("Digite a quantidade de peças 2:")
   Leia(QP2)
   Escreva("Digite de percentagem que será acrescentado sobre o valor das peças:")
   Leia(IPI)
   VT := (VU1*QP1+VU2*QP2)*(IPI/100+1)
   Escreva(" O valor total é:", VT)
   
   

Fimalgoritmo