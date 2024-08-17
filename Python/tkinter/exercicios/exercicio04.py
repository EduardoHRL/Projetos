from tkinter import *

class aplicativo:
    def __init__(self, master = None):
        self.container = Frame(master)
        self.container.pack()

        self.botao1 = Button()
        self.botao1["text"] = "1"
        self.botao1.pack()

        self.botao2 = Button()
        self.botao2["text"] = "2"
        self.botao2.pack()

        self.botao3 = Button()
        self.botao3["text"] = "3"
        self.botao3.pack()

        self.botao4 = Button()
        self.botao4["text"] = "4"
        self.botao4.pack()

        self.botao5 = Button()
        self.botao5["text"] = "5"
        self.botao5.pack()

        self.botao6 = Button()
        self.botao6["text"] = "6"
        self.botao6.pack()


root = Tk()
aplicativo(root)
root.mainloop()