algoritmo "soma_!00"
var
   A, cont, S1, S2 : INTEIRO
inicio
      enquanto (cont <=10) faca
               escreva("digite um número:")
               leia (A)
               se (cont<=5) E (A%2=0) entao
                  S1 <- S1 + A
                  cont <- cont + 1
               senao
                     se(cont>5) E (A%2=0) entao
                        S2 <- S2 + A
                        cont <- cont + 1
                        fimse
      fimenquanto
      escreva(S1)
      ESCREVA(S2)
fimalgoritmo
               