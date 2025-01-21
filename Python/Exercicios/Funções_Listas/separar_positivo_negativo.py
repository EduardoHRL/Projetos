listaNegativo = list()
listaPositivo = list()

for i in range(10):
    elem = int(input("Digite um número positivo ou negativo: "))
    if elem >= 0:
        listaPositivo.append(elem)
    else:
        listaNegativo.append(elem)

print("Numeros positivos:",listaPositivo)
print("Numero negativos:",listaNegativo)

