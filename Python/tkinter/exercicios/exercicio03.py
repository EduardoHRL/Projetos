from tkinter import *

class aplicativo():
    def __init__(self, master = None):
        self.container = Frame(master)
        self.container.pack()

        self.nome = Label(text="Insira seu nome:")
        self.nome.pack()
        self.campo = Entry()
        self.campo.pack()

        self.botao = Button()
        self.botao["text"] = "Confirmar"
        self.botao["command"] = self.bemVindo
        self.botao.pack()

        self.frase = Label(text="")
        self.frase.pack()

    def bemVindo(self):
        nome = self.campo.get()
        self.frase["text"] = "Olá", nome

root = Tk()
aplicativo(root)
root.mainloop()