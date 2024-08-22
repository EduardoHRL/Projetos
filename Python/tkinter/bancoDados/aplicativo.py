from tkinter import *

from usuarios import *

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
        self.botaoID["command"] = self.buscarUsuario
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
        self.botInsert["command"] = self.inserirUsuario
        self.botInsert.pack(side = LEFT)

        self.botAlterar = Button(self.setimoContainer, text = "Alterar", width = 12)
        self.botAlterar["command"] = self.alterarUsuario
        self.botAlterar.pack(side = LEFT)

        self.botExcluir = Button(self.setimoContainer,text = "Excluir", width = 12)
        self.botExcluir["command"] = self.excluirUsuario
        self.botExcluir.pack(side = LEFT)

        self.botLimpar = Button(self.setimoContainer, text = "Limpar", width = 12)
        self.botLimpar["command"] = self.Limpar
        self.botLimpar.pack(side = LEFT)

        self.msg = Label(text = "")
        self.msg.pack()

    def Limpar(self):
        self.entID.delete(0, END)
        self.entNome.delete(0, END)
        self.entTelefone.delete(0, END)
        self.entEmail.delete(0, END)
        self.entUsuario.delete(0, END)
        self.entSenha.delete(0, END)

    def inserirUsuario(self):
        user = usuarios()

        user.nome = self.entNome.get()
        user.telefone = self.entTelefone.get()
        user.email = self.entEmail.get()
        user.usuario = self.entUsuario.get()
        user.senha = self.entSenha.get()

        self.entID.delete(0, END)
        self.entNome.delete(0, END)
        self.entTelefone.delete(0, END)
        self.entEmail.delete(0, END)
        self.entUsuario.delete(0, END)
        self.entSenha.delete(0, END)

        self.msg["text"] = user.insertUser()

    def alterarUsuario(self):
        user = usuarios()

        self.msg["text"] = user.updateUser()

        user.id = self.entID.get()
        user.nome = self.entNome.get()
        user.telefone = self.entTelefone.get()
        user.email = self.entEmail.get()
        user.usuario = self.entUsuario.get()
        user.senha = self.entSenha.get()

        self.entID.delete(0, END)
        self.entNome.delete(0, END)
        self.entTelefone.delete(0, END)
        self.entEmail.delete(0, END)
        self.entUsuario.delete(0, END)
        self.entSenha.delete(0, END)

        self.msg["text"] = user.updateUser()

    def excluirUsuario(self):
        user = usuarios()

        user.id = self.entID.get()

        self.msg["text"] = user.deleteUser()

        self.entID.delete(0, END)
        self.entNome.delete(0, END)
        self.entTelefone.delete(0, END)
        self.entEmail.delete(0, END)
        self.entUsuario.delete(0, END)
        self.entSenha.delete(0, END)

    def buscarUsuario(self):
        user = usuarios()

        user.id = self.entID.get()

        self.msg["text"] = user.selectUser()

        self.entID.delete(0, END)
        self.entID.insert(INSERT, user.id)

        self.entNome.delete(0, END)
        self.entNome.insert(INSERT, user.nome)

        self.entTelefone.delete(0, END)
        self.entTelefone.insert(INSERT,user.telefone)

        self.entEmail.delete(0, END)
        self.entEmail.insert(INSERT, user.email)

        self.entUsuario.delete(0, END)
        self.entUsuario.insert(INSERT, user.usuario)

        self.entSenha.delete(0, END)
        self.entSenha.insert(INSERT,user.senha)

        
if __name__ == "__main__":
    root = Tk()
    aplicativo(root)
    root.mainloop()