import sqlite3

class banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.conexao.execute("PRAGMA foreign_keys = ON")
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
                  cidade text,
                  estado text
                  )""")
        c.execute("""create table if not exists clientes (
                  id integer primary key autoincrement,
                  nome text,
                  telefone text,
                  email text,
                  endereco text,
                    cpf text,
                  cidade integer,
                  FOREIGN KEY (id) REFERENCES cidades(id) ON DELETE RESTRICT
                  )""")
      
        self.conexao.commit()
        c.close()
    
    
                