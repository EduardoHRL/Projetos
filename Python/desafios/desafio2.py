class Estado():
    def __init__(self, cidades, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = cidades

    def add_cidade(self, nome, estado, populacao):
        self.cidades.append(nome, estado, populacao)

    def resumo(self):
        print("\nEstado:",self.nome,"\n")
        for cidade in self.cidades:
            print("Cidade:",cidade.nome,
                  "\nPopulacao:",cidade.populacao,"\n")
        print("Populacao Total:",Estado.soma(self))
    def soma(self):
        return sum([c.populacao for c in self.cidades])


class Cidade():
    def __init__(self, nome, populacao: int):
        self.nome = nome
        self.populacao = populacao
        self.estado = ""




cidade = Cidade("Canapolis",15000)
cidade2 = Cidade("Cachoeira Dourada", 267000)
cidade3 = Cidade("Itumbiara",125765)

minas = Estado({cidade, cidade2},"Minas Gerais", "MG")
goias = Estado({cidade3},"Goias","GO")

minas.resumo()