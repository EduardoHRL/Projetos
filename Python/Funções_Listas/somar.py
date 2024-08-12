def somar_entre_50_100():
    n = 50
    soma = 0
    while n >= 50 and n <= 100:
        if n % 2 == 0:
            soma += n
        n += 1
    print(soma)

somar_entre_50_100()



