algoritmo "cpf"
var
   vet : vetor[1..11] de inteiro
   dig1 , dig2, s , res, i : inteiro
inicio
   para i de 1 ate 11 faca
      escreval("Digite o ",i,"° digito do cpf:")
      leia(vet[i])
   fimpara
   para i de 1 ate 9 faca
      s := s + vet[i] * (11-i)
   fimpara
   res := s % 11
   se res < 2 entao
      dig1 := 0
      senao
         dig1 := 11 - res
   fimse
   s := 0
   para i de 1 ate 9 faca
      s := s + vet[i] * (12 - i)
   fimpara
   s := s + dig1 * 2
   res := s % 11
   se res < 2 entao
      dig2 := 0
      senao
         dig2 := 11 - res
   fimse
   se (vet[10] = dig1) e (vet[11] = dig2) entao
      escreval("O cpf está correto")
      senao
         escreval("os digitos verificadores corretos são: ", dig1 , dig2)
   fimse
   
   
   se (vet[9] = 0) entao
      escreval("O seu cpf é do Rio Grande Do Sul - RS")
      senao
           se (vet[9] = 1) entao
      escreval("O seu cpf pode ser de Goias, Distrito Federal, Mato Grosso, Mato Grosso do Sul ou Tocantins")
      senao
           se (vet[9] = 2) entao
      escreval("O seu cpf pode ser do Pará, Amazonas, Acre, Amapa, Rondônia ou Roraima")
      senao
           se (vet[9] = 3) entao
      escreval("O seu cpf pode ser do Ceará, Maranhão ou Piaui")
      senao
           se (vet[9] = 4) entao
      escreval("O seu cpf pode ser do Pernambuco, Rio Grande do Norte, Paraiba ou Alagoas")
      senao
           se (vet[9] = 5) entao
      escreval("O seu cpf pode ser do Bahia ou Sergipe")
      senao
           se (vet[9] = 6) entao
      escreval("O seu cpf é de Minas Gerais")
      senao
           se (vet[9] = 7) entao
      escreval("O seu cpf é do Rio de Janeiro ou Espirito Santo")
      senao
           se (vet[9] = 8) entao
      escreval("O seu cpf é de São Paulo")
      senao
           se (vet[9] = 9) entao
      escreval("O seu cpf é de Santa ou Paraná")
           Fimse
           fimse
           fimse
           fimse
           fimse
           fimse
           fimse
           fimse
           fimse
      fimse



      
fimalgoritmo
   