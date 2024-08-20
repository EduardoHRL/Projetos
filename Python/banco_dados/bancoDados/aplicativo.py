from tkinter import *


class aplicativo:
    def __init__(self, master = None):
        self.fontePadrao = ("Arial", "10")
        
        self.primeiroContainer = Frame(master)
        self.primeiroContainer.pack(pady = 20)

        self.segundoContainer = Frame(master)
        self.segundoContainer.pack(pady = 5)

        self.terceiroContainer = Frame(master)
        self.terceiroContainer.pack(pady = 5)

        self.quartoContainer = Frame(master)
        self.quartoContainer.pack(pady = 5)

        self.quintoContainer = Frame(master)
        self.quintoContainer.pack(pady = 5)

        self.sextoContainer = Frame(master)
        self.sextoContainer.pack(pady = 5)

        self.cad = Label(self.primeiroContainer, text = "Cadastro de Usuarios")
        self.cad.pack()

        self.txtNome = Label(self.segundoContainer,text = "Nome: ", font = self.fontePadrao)
        self.txtNome.pack(side = LEFT)
        self.entNome = Entry(self.segundoContainer)
        self.entNome.pack()

        self.txtTelefone = Label(self.terceiroContainer,text = "Telefone:", font = self.fontePadrao)
        self.txtTelefone.pack(side = LEFT)
        self.entTelefone = Entry(self.terceiroContainer)
        self.entTelefone.pack()

        self.txtEmail = Label(self.quartoContainer,text = "Email:", font = self.fontePadrao)
        self.txtEmail.pack(side=LEFT)
        self.entEmail = Entry(self.quartoContainer)
        self.entEmail.pack()

        self.txtUsuario = Label(self.quintoContainer, text = "Usuario: ", font = self.fontePadrao)
        self.txtUsuario.pack(side = LEFT)
        self.entUsuario = Entry(self.quintoContainer)
        self.entUsuario.pack()

        self.txtSenha = Label(self.sextoContainer, text = "Senha: ", font = self.fontePadrao)
        self.txtSenha.pack(side = LEFT)
        self.entSenha = Entry(self.sextoContainer)
        self.entSenha.pack()



root = Tk()
aplicativo(root)
root.mainloop()