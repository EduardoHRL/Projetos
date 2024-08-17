from tkinter import *
class aplicativo:
    def __init__(self, master = None):
        self.container = Frame(master)
    
        self.container.pack()
        self.label1 = Label(self.container, text="label 1")
        self.label1.pack(side = TOP, padx = 0, pady = 0)

        self.label2 = Label(text="label 2")
        self.label2.pack(side = BOTTOM)

        self.label3 = Label(text="label 3")
        self.label3.pack(side = LEFT)

        self.label4 = Label(text="label 4")
        self.label4.pack(side = RIGHT)

root = Tk()
aplicativo(root)
root.mainloop()
