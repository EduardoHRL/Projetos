algoritmo " divisivel por outro"
// Disciplina   : [Linguagem e Lógica de Programação] 
// Professor   : Antonio Carlos Nicolodi 
var
   N1, N2 : INTEIRO
   ND : REAL
inicio
      escreval ("Digite um número:")
      leia(N1)
      escreval ("Digite outro número:")
      leia(N2)
      ND := N1/N2
      SE (N1%N2=0) ENTAO
         escreval("o número" ,N1, " é divisivel por" ,N2)
      SENAO
           escreval("o número", N1, " não é divisivel por" ,N2)
      fimse
      escreval ("a divisão final é:",ND)
fimalgoritmo