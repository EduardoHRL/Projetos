algoritmo "soma_!00"
var
   A, cont, S1, S2 : INTEIRO
inicio
      enquanto (cont <10) faca
               escreva("digite um n�mero:")
               leia (A)
               se (cont<5) E (A%2=0) entao
                  S1 <- S1 + A
               senao
                    se(cont >= 5) E (A%2<>0) entao
                        S2 <- S2 + A
                        fimse
              fimse
              cont <- cont + 1

      fimenquanto
      escreva(S1)
      ESCREVA(S2)
fimalgoritmo
               