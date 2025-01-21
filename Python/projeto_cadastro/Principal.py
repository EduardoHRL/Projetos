from tkinter import *
from tkinter import filedialog
from usuarios import *
from cidades import *
from clientes import *

class Home:
    def __init__(self, master = None):
        self.root = Tk()
        self.root.title("Início")
        self.root.state('zoomed')

        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        self.filemenu = Menu(self.menubar)
        self.filemenu2 = Menu(self.menubar)
        self.filemenu3 = Menu(self.menubar)

        self.menubar.add_cascade(label='Arquivo', menu=self.filemenu)
        self.menubar.add_cascade(label='Cadastros', menu=self.filemenu2)
        self.menubar.add_cascade(label='Ajuda', menu=self.filemenu3)

        self.container = Frame(self.root)
        self.container.pack(fill=BOTH, expand=True)

        self.create_menu()

    def create_menu(self):
        def clear_frame():
            for widget in self.container.winfo_children():
                widget.destroy()

        def abrirUsuarios():
            clear_frame()
            app = cadastro(master=self.container)
            app.pack(fill=BOTH, expand=True)

        def abrirCidades():
            clear_frame()
            app = cidades(master=self.container)
            app.pack(fill=BOTH, expand=True)

        def abrirClientes():
            clear_frame()
            app = appClientes(master=self.container)
            app.pack(fill=BOTH, expand=True)

        def Open():
            filedialog.askopenfilename()

        def Save():
            filedialog.asksaveasfilename()

        def Quit():
            self.root.destroy()

        def Help():
            clear_frame()
            text = Text(self.container)
            text.pack(fill=BOTH, expand=True)
            text.insert('insert', 'Essa página abrirá três cadastros: Usuários, Cidades e Clientes')

        self.filemenu.add_command(label='Abrir...', command=Open)
        self.filemenu.add_command(label='Salvar como...', command=Save)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Sair', command=Quit)
        self.filemenu2.add_command(label='Usuários', command=abrirUsuarios)
        self.filemenu2.add_command(label='Cidades', command=abrirCidades)
        self.filemenu2.add_command(label='Clientes', command=abrirClientes)
        self.filemenu3.add_command(label='Ajuda', command=Help)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    home = Home()
    home.run()
