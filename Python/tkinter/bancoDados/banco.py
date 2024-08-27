import sqlite3

class banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()
    
    def createTable(self):
        c = self.conexao.cursor()


        c.execute("""create table if not exists usuarios (
                  id integer primary key autoincrement,
                  nome text,
                  telefone text,
                  email text,
                  usuario text,
                  senha text
                  )""")
        c.execute("""create table if not exists cidades (
                  id integer primary key autoincrement,
                  nome text,
                  estado text
                  )""")
        c.execute("""create table if not exists clientes (
                  id integer primary key autoincrement,
                  cpf text,
                  nome text,
                  telefone text,
                  email text,
                  endereco text
                  )""")
      
        self.conexao.commit()
        c.close()
    
    
                