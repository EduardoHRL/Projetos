nome = "Eduardo Henrique Rodrigues Lopes"
altura = 2
peso = 130 
imc = peso / altura ** 2

# f-strings
linha_1 = f"{nome} tem {altura} metros de altura,"
linha_2 = f"pesa {peso:.2f} quilos,"
linha_3 = f"e seu IMC é {imc}"

print(linha_1)
print(linha_2)
print(linha_3)