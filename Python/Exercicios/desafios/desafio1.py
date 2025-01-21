#Criação da classe Cliente
class Cliente():

    #Criação do construtor
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


#Criação da classe Conta
class Conta(Cliente):
    #Criação do construtor
    def __init__(self, clientes, número,saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.deposito(saldo)

    #Metodo que imprime o numero e saldo da conta
    def resumo(self):
        print(f"CC N°{self.número} Saldo: {self.saldo:10.2f}")

        for cliente in self.clientes:
            print("Nome:",cliente.nome)
            print("Telefone:",cliente.telefone)
            

    #Metodo de saque.
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
        else:
            print("Saldo insuficiente!")

    #Metodo de deposito.
    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])

    #Metodo que mostra o extrato da conta.
    def extrato(self):
        print(f"Extrato CC N° {self.número}\n")
        for o in self.operações:
            print(f"{o[0]:10s} {o[1]:10.2f}")
            print(f"\n Saldo: {self.saldo:10.2f}\n")

#Criação da classe ContaEspecial herdando da classe Conta
class ContaEspecial(Conta):

    #Criação do construtor
    def __init__(self, clientes, número, saldo=0, limite=0):
        Conta.__init__it__(self, clientes, número, saldo)
        self.limite = limite

    #Metodo de saque, diferente da classe Conta o saque pode ser feito com limite.
    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
        else:
            Conta.saque(self, valor)

cliente1 = Cliente("Joao","1234-5678")
cliente2 = Cliente("Maria","8765-4321")

contaJoao = Conta([cliente1],1234, 5000)
contaMaria = Conta([cliente2], 4321, 1000)

contaJoao.saque(2500)

contaJoao.resumo()
contaMaria.resumo()


    