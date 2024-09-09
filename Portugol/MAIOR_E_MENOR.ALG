Algoritmo "Maior_e_menor"
 Var
    N1, N2, N3, MAIOR, MEIO, MENOR : REAL
 Inicio
       Escreva("Digite o primeiro numero:")
       Leia(N1)
       Escreva("Digite o segundo numero:")
       Leia(N2)
       Escreva("Digite o terceiro numero:")
       Leia(N3)
       Se (N1>N2) E (N1>N3) ENTAO
          MAIOR:= N1
          SE (N2>N3) ENTAO
             MEIO := N2
             MENOR := N3
          SENAO
               MEIO := N3
               MENOR := N2
          FIMSE
       SENÃO
            SE (N2>N1) E (N2>N3) ENTAO
                MAIOR := N2
                SE (N1>N3) ENTAO
                MEIO := N1
                 MENOR := N3
                SENAO
                MEIO :=N3
                MENOR := N1
                FIMSE
       SENAO
            MAIOR := N3
            SE (N2>N1) ENTAO
            MEIO := N2
            MENOR := N1
            SENAO
            MEIO := N1
            MENOR := N2
       FIMSE
       FIMSE
       FIMSE
       Escreva("Os numeros em ordem são:",MAIOR," ",MEIO," ",MENOR)
       
FIMALGORITMO