Algoritmo "alistamento"
 Var
    AN, AA, DA, KA, A, B : INTEIRO
 Inicio
       Escreva ("Digite o ano de nascimento da pessoa:")
       Leia(AN)
       KA := 2023-AN
       
       SE (KA>18) ENTAO
          A := KA-18
          Escreva("passaram" ,A, " ", "ANOS do alistamento")

       SENAO
            SE (KA<18) ENTAO
               B := 18-KA
               ESCREVA("Faltam" ,B, " ", "ANOS para o alistamento")
            FIMSE
       FIMSE
fimalgoritmo
                    
