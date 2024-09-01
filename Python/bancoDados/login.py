from tkinter import *
from banco import *
from tkinter import messagebox
from Principal import *
import usuarios

class login:
    def __init__(self, master = None):
        self.master = master
        self.container = Frame(master)
        self.container.pack(pady = 20)

        self.container02 = Frame(master)
        self.container02.pack(pady = 5, padx = 20)

        self.container03 = Frame(master)
        self.container03.pack(pady = 5, padx = 20)

        self.container04 = Frame(master)
        self.container04.pack(pady = 5, padx = 20)

        self.titulo = Label(self.container, text = "Login")
        self.titulo.pack()

        self.txtUsuario = Label(self.container02, text = "Usuario")
        self.txtUsuario.pack(side = LEFT)

        self.entUsuario = Entry(self.container02)
        self.entUsuario.pack(side = LEFT)

        self.txtSenha = Label(self.container03, text = "Senha")
        self.txtSenha.pack(side = LEFT)

        self.entSenha = Entry(self.container03, show = "*")
        self.entSenha.pack(side = LEFT)

        self.botao = Button(self.container04,text = "Entrar", width = 10, command = self.logar)
        self.botao.pack()

        self.msg = Label(text = "")
        self.msg.pack()

        self.txtCadastro = Label(text = "Não tem cadastro?")
        self.txtCadastro.pack(pady = 10)

        self.bntCadastro = Button(text = "Cadastrar", width = 10, command = self.abrir_cadastro)
        self.bntCadastro.pack()

    def logar(self):
        b = banco()
        c = b.conexao.cursor()

        usu = self.entUsuario.get()
        senha = self.entSenha.get()

        c.execute("SELECT usuario, senha FROM usuarios WHERE usuario = ? AND senha = ?", (usu, senha))

        usu_found = c.fetchone()

        c.close()

        if usu_found:
            self.master.destroy()
            self.abrir_principal()
        else:
            self.msg["text"] = "Usuário e/ou senha incorretos"

    def abrir_principal(self):
        app = Home(master= root)
        app.run()

    def abrir_cadastro(self):
        self.master.destroy() 
        app = cadastro(master= Tk())

if __name__ == "__main__":
    root = Tk()
    root.title("Login")
    root.geometry("300x250")
    root.geometry("+500+210")
    root.resizable(False, False)
    login(root)
    root.mainloop()
