algoritmo " divisivel por outro"
// Disciplina   : [Linguagem e L�gica de Programa��o] 
// Professor   : Antonio Carlos Nicolodi 
var
   N1, N2 : INTEIRO
   ND : REAL
inicio
      escreval ("Digite um n�mero:")
      leia(N1)
      escreval ("Digite outro n�mero:")
      leia(N2)
      ND := N1/N2
      SE (N1%N2=0) ENTAO
         escreval("o n�mero" ,N1, " � divisivel por" ,N2)
      SENAO
           escreval("o n�mero", N1, " n�o � divisivel por" ,N2)
      fimse
      escreval ("a divis�o final �:",ND)
fimalgoritmo