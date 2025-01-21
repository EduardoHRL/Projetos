from banco import banco

class cliente(object):

    def __init__(self,id= 0, nome = "", telefone ="", email = "", endereco = "",cpf = "", cidade = ""):
        self.info = {}
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.cpf = cpf
        self.cidade = cidade

    def insertCliente(self):
        b = banco()
        try:
            c = b.conexao.cursor()

            c.execute("insert into clientes(nome, telefone, email, endereco,cpf, cidade) values ('"+self.nome+"', '"+self.telefone+"', '"+self.email+"', '"+self.endereco+"', '"+self.cpf+"', '"+self.cidade+"')")
            b.conexao.commit()

            c.close()
            return "Cliente cadastrado com sucesso!"
        except:
            return "Ocorreu um erro"
        
    def updateCliente(self):
        b = banco()
        try:
            c = b.conexao.cursor()

            c.execute("update clientes set nome = '" + self.nome+ "', telefone = '"+self.telefone+"', email = '"+self.email+"', endereco = '"+self.endereco+"', cpf = '"+self.cpf+"', cidade = '"+self.cidade+"' where id = "+self.id+" ")


            b.conexao.commit()
            c.close()

            return "Cliente atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do cliente!"
        
    def deleteCliente(self):
        b = banco()
        try:
            c = b.conexao.cursor()

            c.execute("delete from clientes where id = "+self.id+" ")

            b.conexao.commit()

            c.close()

            return "Cliente excluido com sucesso"
        except:
            return "Cliente nao foi excluido"
        
    def selectCliente(self):
        b = banco()
        try:
            c = b.conexao.cursor()

            c.execute("select * from clientes where id = "+self.id+" ")

            for linha in c:
                self.id = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.endereco = linha[4]
                self.cpf = linha[5]
                self.cidade = linha[6]

            c.close()
            return "Cliente buscado com sucesso"
        except:
            return "Busca não efetuada com sucesso"
        
    def buscarTreeView(self):
        b = banco()
        c = b.conexao.cursor()
        
        c.execute("SELECT * FROM clientes")

        rows = []

        for linha in c:
            rows.append((linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6]))

        c.close()
        
        return rows
    
    def buscarComboBox(self):
        b = banco()
        c = b.conexao.cursor()

        c.execute("select cidade FROM cidades")

        resultado = []

        for linha in c:
            resultado.append(linha[0])

        c.close()
        return resultado