Algoritmo "Media"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 19/05/2023
Var
// Se��o de Declara��es das vari�veis 
N1, N2, N3, TM, PO, AR, MA, MP, TMEDIA   : REAL
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
   Escreva ("Digite a primeira nota:")
   Leia(N1)
   Escreva ("Digite a segunda nota:")
   Leia(N2)
   Escreva ("Digite a terceira nota:")
   Leia(N3)
   Escreva(" Se deseja a media aritmetica digite 1, se deseja ponderada digite 2:")
   Leia(TMEDIA)
   SE (TMEDIA=1) Entao
     MA := (N1+N2+N3)/3
     Escreva ("A media aritmetica �:", MA)
   Fimse
   SE (TMEDIA=2) Entao
      MP := ((N1*3)+(N2*3)+(N3*4))/10)
      Escreva ("A Media ponderada �:",MP)
   Fimse
   

   
Fimalgoritmo