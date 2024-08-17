from tkinter import *
from math import *
class aplicativo:
    def __init__(self, master = None):
        self.container = Frame(master)
        self.container.pack()
        self.titulo = Label(self.container, text="soma")
        self.titulo.pack()

        self.label1 = Label(text="Primeiro valor:")
        self.label1.pack()
        self.primeiro = Entry()
        self.primeiro.pack()

        self.label2 = Label(text="Segundo valor:")
        self.label2.pack()
        self.segundo = Entry()
        self.segundo.pack()

        self.botao = Button()
        self.botao["text"] = "Somar"
        self.botao["command"] = self.somar
        self.botao.pack()

        self.resultado = Label(text="Resultado:")
        self.resultado.pack()
        self.result = Label(text="")
        self.result.pack()
    def somar(self):
        n1 = self.primeiro.get()
        n2 = self.segundo.get()
        numero1 = int(n1)
        numero2 = int(n2)
        resultado = numero1 + numero2
        self.result["text"] = resultado

root = Tk()
aplicativo(root)
root.mainloop()
