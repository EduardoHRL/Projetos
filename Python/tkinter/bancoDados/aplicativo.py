from tkinter import *

from tkinter.bancoDados import bancoDados

class aplicativo:
    def __init__(self, master = None):
        self.fontePadrao = ("Arial", "10")
        
        self.primeiroContainer = Frame(master)
        self.primeiroContainer.pack(pady = 20)

        self.container = Frame(master)
        self.container.pack(pady = 5, padx = 20)

        self.segundoContainer = Frame(master)
        self.segundoContainer.pack(pady = 5, padx = 20)

        self.terceiroContainer = Frame(master)
        self.terceiroContainer.pack(pady = 5, padx = 20)

        self.quartoContainer = Frame(master)
        self.quartoContainer.pack(pady = 5, padx = 20)

        self.quintoContainer = Frame(master)
        self.quintoContainer.pack(pady = 5, padx = 20)

        self.sextoContainer = Frame(master)
        self.sextoContainer.pack(pady = 5, padx = 20)

        self.setimoContainer = Frame(master)
        self.setimoContainer.pack(pady = 10, padx = 20)

        self.cad = Label(self.primeiroContainer, text = "Cadastro de Usuarios")
        self.cad.pack()

        self.buscarID = Label(self.container, text = "Buscar ID:", font = self.fontePadrao)
        self.buscarID.pack(side = LEFT)
        self.entID = Entry(self.container)
        self.entID["width"] = 5
        self.entID.pack(side = LEFT)
        self.botaoID = Button(self.container,text = "Buscar")
        self.botaoID.pack(padx = 5)
        

        self.txtNome = Label(self.segundoContainer,text = "Nome: ", font = self.fontePadrao, width = 10)
        self.txtNome.pack(side = LEFT)
        self.entNome = Entry(self.segundoContainer)
        self.entNome["width"] = 25
        self.entNome.pack(side = LEFT)

        self.txtTelefone = Label(self.terceiroContainer,text = "Telefone:", font = self.fontePadrao, width = 10)
        self.txtTelefone.pack(side = LEFT)
        self.entTelefone = Entry(self.terceiroContainer)
        self.entTelefone["width"] = 25
        self.entTelefone.pack()

        self.txtEmail = Label(self.quartoContainer,text = "Email:", font = self.fontePadrao, width = 10)
        self.txtEmail.pack(side=LEFT)
        self.entEmail = Entry(self.quartoContainer)
        self.entEmail["width"] = 25
        self.entEmail.pack()

        self.txtUsuario = Label(self.quintoContainer, text = "Usuario: ", font = self.fontePadrao, width = 10)
        self.txtUsuario.pack(side = LEFT)
        self.entUsuario = Entry(self.quintoContainer)
        self.entUsuario["width"] = 25
        self.entUsuario.pack()

        self.txtSenha = Label(self.sextoContainer, text = "Senha: ", font = self.fontePadrao, width = 10)
        self.txtSenha.pack(side = LEFT)
        self.entSenha = Entry(self.sextoContainer)
        self.entSenha["width"] = 25
        self.entSenha.pack()

        self.botInsert = Button(self.setimoContainer,text="Inserir", width = 12)
        self.botInsert.pack(side = LEFT)

        self.botAlterar = Button(self.setimoContainer, text = "Alterar", width = 12)
        self.botAlterar.pack(side = LEFT)

        self.botExcluir = Button(self.setimoContainer,text = "Excluir", width = 12)
        self.botExcluir.pack(side = LEFT)

        self.botLimpar = Button(self.setimoContainer, text = "Limpar", width = 12)
        self.botLimpar["command"] = self.Limpar
        self.botLimpar.pack(side = LEFT)

    def Limpar(self):
        self.entID.delete(0, END)
        self.entNome["text"]  = ""
        self.entTelefone["text"]  = ""
        self.entEmail["text"]  = ""
        self.entUsuario["text"]  = ""
        self.entSenha["text"]  = ""

    def inserirUsuario(self):
        user = usuarios()



root = Tk()
aplicativo(root)
root.mainloop()