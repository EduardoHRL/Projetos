from tkinter import *
from banco import *
from tkinter import messagebox
from Home import *

class login:
    def __init__(self, master = None):
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

        self.entSenha = Entry(self.container03)
        self.entSenha.pack(side = LEFT)

        self.botao = Button(self.container04,text = "Entrar", width = 10, command = self.abrir_principal)
        self.botao.pack()

        self.msg = Label(text = "")
        self.msg.pack()

    def logar(self):
        b = banco()
        c = b.conexao.cursor()

        c.execute("select usuario from usuarios")
        for linha in c:
            u = linha

        c.execute("select senha from usuarios")
        for linha in c:
            s = linha

        c.close()

        usu = self.entUsuario.get()
        senha = self.entSenha.get()

        if usu in u and senha in s:
            self.msg["text"] = "sim"

        else:
            self.msg["text"] = "nao"
    
    def abrir_principal(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        # Create Home widgets
        home_app = Home(master=self.master)
        home_app.run()

root = Tk()
root.geometry("300x200")
root.resizable(False, False)
login(root)
root.mainloop()
