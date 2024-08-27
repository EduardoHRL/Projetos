from tkinter import *
from usuarios import *
from cidades import *

def abrir_cadastro():
    app = aplicativo(master=janela)
    botao.pack_forget()
    botao2.pack_forget()

def abrir_cadastro_cidades():
    app = cidades(master = janela)
    botao2.pack_forget()
    botao.pack_forget()

janela = Tk()

botao = Button(janela, text="Abrir Cadastro de Usuários", command=abrir_cadastro)
botao.pack()

botao2 = Button(janela, text="Abrir cadastro de cidades", command=abrir_cadastro_cidades)
botao2.pack()


janela.mainloop()
