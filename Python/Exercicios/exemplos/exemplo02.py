numero = int(input("Digite um número menor que 100: "))

if numero >= 100:
    print("O numero digitado deve ser menor que 100")
else:
    dezena = numero // 10
    unidade = numero % 10
    soma = dezena + unidade
    print("Soma:",soma)