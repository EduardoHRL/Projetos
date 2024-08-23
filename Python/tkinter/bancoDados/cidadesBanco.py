from banco import banco

class cid(object):

    def __init__(self, nome = "", estado =""):
        self.info = {}
        self.nome = nome
        self.estado  = estado

    def cadastrarCidade(self):
        b = banco()
        try:
            c = b.conexao.cursor()

            c.execute("insert into cidades(nome, estado) values ('"+self.nome+"', '"+self.estado+"')")
            b.conexao.commit()

            c.close()
            return "Cidade cadastrada com sucesso!"
        except:
            return "Ocorreu um erro"