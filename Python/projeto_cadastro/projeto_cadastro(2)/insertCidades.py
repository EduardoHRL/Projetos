from banco import banco

class cid(object):

    def __init__(self,id= 0 , cidade = "", estado =""):
        self.info = {}
        self.id = id
        self.cidade = cidade
        self.estado  = estado

    def cadastrarCidade(self):
        b = banco()
        try:
            c = b.conexao.cursor()

            c.execute("insert into cidades(cidade, estado) values ('"+self.cidade+"', '"+self.estado+"')")
            b.conexao.commit()

            c.close()
            return "Cidade cadastrada com sucesso!"
        except:
            return "Ocorreu um erro"
        
    def updateCidade(self):
        b = banco()
        try:
            c = b.conexao.cursor()

            c.execute("update cidades set cidade = '" + self.cidade+ "', estado = '"+self.estado+"' where id = "+self.id+" ")


            b.conexao.commit()
            c.close()

            return "Cidade atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração da cidade!"
        
    def deleteCidade(self):
        b = banco()
        try:
            c = b.conexao.cursor()

            c.execute("delete from cidades where id = "+self.id+" ")

            b.conexao.commit()

            c.close()

            return "Cidade excluida com sucesso"
        except:
            return "Cidade nao foi excluida"
        
    def buscarCidade(self):
        b = banco()
        try:
            c = b.conexao.cursor()

            c.execute("select * from cidades where id = "+self.id+" ")

            for linha in c:
                self.id = linha[0]
                self.cidade = linha[1]
                self.estado = linha[2]

            c.close()
            return "Cidade buscada com sucesso"
        except:
            return "Busca não efetuada com sucesso"
        
    def buscarTreeView(self):
        b = banco()
        c = b.conexao.cursor()
        
        c.execute("SELECT * FROM cidades")

        rows = []

        for linha in c:
            rows.append((linha[0], linha[1], linha[2]))

        c.close()
        
        return rows
