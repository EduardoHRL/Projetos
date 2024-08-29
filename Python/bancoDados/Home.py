from tkinter import *
from tkinter import filedialog
from usuarios import *
from cidades import *
from clientes import *

root = Tk()
menubar = Menu(root)
root.config(menu=menubar)

root.title("Inicio")
root.state('zoomed')

filemenu = Menu(menubar)
filemenu2 = Menu(menubar)
filemenu3 = Menu(menubar)

menubar.add_cascade(label='Arquivo', menu=filemenu)
menubar.add_cascade(label='Cadastros', menu=filemenu2)
menubar.add_cascade(label='Ajuda', menu=filemenu3)

# Frame para exibir o conteúdo
container = Frame(root)
container.pack(fill=BOTH, expand=True)

def clear_frame():
    for widget in container.winfo_children():
        widget.destroy()

def abrirUsuarios():
    clear_frame()
    app = aplicativo(master=container)
    app.pack(fill=BOTH, expand=True)

def abrirCidades():
    clear_frame()
    app = cidades(master=container)
    app.pack(fill=BOTH, expand=True)

def abrirClientes():
    clear_frame()
    app = appClientes(master=container)
    app.pack(fill=BOTH, expand=True)

def Open():
    filedialog.askopenfilename()

def Save():
    filedialog.asksaveasfilename()

def Quit():
    root.destroy()

def Help():
    clear_frame()
    text = Text(container)
    text.pack(fill=BOTH, expand=True)
    text.insert('insert', 'Essa página abrirá três cadastros: Usuários, Cidades e Clientes')

filemenu.add_command(label='Abrir...', command=Open)
filemenu.add_command(label='Salvar como...', command=Save)
filemenu.add_separator()
filemenu.add_command(label='Sair', command=Quit)
filemenu2.add_command(label='Usuários', command=abrirUsuarios)
filemenu2.add_command(label='Cidades', command=abrirCidades)
filemenu2.add_command(label='Clientes', command=abrirClientes)
filemenu3.add_command(label='Ajuda', command=Help)

root.mainloop()
