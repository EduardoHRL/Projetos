from tkinter import *
from aplicativo import aplicativo

def abrir_cadastro():
    app = aplicativo(master=janela)
    botao.pack_forget()


janela = Tk()


botao = Button(janela, text="Abrir Cadastro de Usuários", command=abrir_cadastro)
botao.pack()


janela.mainloop()
