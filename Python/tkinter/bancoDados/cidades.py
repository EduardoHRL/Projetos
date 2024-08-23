from tkinter import *
from cidadesBanco import *

class cidades():
    def __init__(self, master = None):
        self.container01 = Frame(master)
        self.container01.pack(pady = 20)
        
        self.container02 = Frame(master)
        self.container02.pack(pady = 5, padx = 20)
        
        self.container03 = Frame(master)
        self.container03.pack(pady = 5, padx = 20)

        self.container04 = Frame(master)
        self.container04.pack(pady = 10)

        self.titulo = Label(self.container01, text = "Cadastro de cidades")
        self.titulo.pack()

        self.txtNome = Label(self.container02, text = "Nome:")
        self.txtNome.pack(side = LEFT)

        self.entNome = Entry(self.container02)
        self.entNome.pack(side = LEFT)

        self.txtEstado = Label(self.container03, text = "Estado:")
        self.txtEstado.pack(side = LEFT)

        self.entEstado = Entry(self.container03)
        self.entEstado.pack(side = LEFT)

        self.botao = Button(self.container04, text = "Cadastrar", width = 12)
        self.botao["command"] = self.cadastrar
        self.botao.pack(side = LEFT)

        self.msg = Label(text = "")
        self.msg.pack()

    def cadastrar(self):
        c = cid()

        self.msg["text"] = c.cadastrarCidade
        c.nome = self.entNome.get()
        c.estado = self.entEstado.get()

        self.entNome.delete(0, END)
        self.entEstado.delete(0, END)

        


root = Tk()
cidades(root)
root.mainloop()