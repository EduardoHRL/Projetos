algoritmo "soma_30"
var
   N, S10, S20, S30, cont : INTEIRO
inicio
      cont <- 0
      enquanto (cont < 30) faca
               escreval ("digite um n�mero:")
               leia(N)
               se (cont < 10) entao
                  S10 <- S10 + N
                  cont <- cont + 1
               senao
                    se (cont < 20) entao
                       S20 <- S20 + N
                       cont <- cont + 1
                    senao
                         se (cont < 30) entao
                         S30 <- S30 + N
                         cont <- cont + 1
                         fimse
                    fimse
               fimse
      fimenquanto
      escreval(" A soma dos 10 n�meros �:", S10)
      escreval(" A soma dos 20 n�meros �:", S20)
      escreval(" A soma dos 30 n�meros �:", S30)
fimalgoritmo