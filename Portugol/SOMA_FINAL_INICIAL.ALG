algoritmo "Soma_Final_Inicial"
var
   i, F, Cont, VT : INTEIRO
inicio
      escreva ("Digite o n�mero inicial:")
      leia (i)
      escreva ("Digite o n�mero final:")
      leia(F)
      enquanto (i < F) faca
               i <- i + 1
               VT <- VT + i
      fimenquanto
      VT <- VT - F
      escreval("A soma total �:", VT)
fimalgoritmo

inicial 2
final 5
vt  2