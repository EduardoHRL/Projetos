from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from insertClientes import *


class appClientes:
    def __init__(self, master = None):
        self.fontePadrao = ("Arial", "10")

        self.primeiroContainer = Frame(master)
        self.primeiroContainer.pack(pady = 20)

        self.container = Frame(master)
        self.container.pack(pady = 5, padx = 20)

        self.segundoContainer = Frame(master)
        self.segundoContainer.pack(pady = 5, padx = 20)

        self.terceiroContainer = Frame(master)
        self.terceiroContainer.pack(pady = 5, padx = 20)

        self.quartoContainer = Frame(master)
        self.quartoContainer.pack(pady = 5, padx = 20)

        self.quintoContainer = Frame(master)
        self.quintoContainer.pack(pady = 5, padx = 20)

        self.sextoContainer = Frame(master)
        self.sextoContainer.pack(pady = 5, padx = 20)

        self.containerComboBox = Frame(master)
        self.containerComboBox.pack(pady = 5, padx = 20)

        self.setimoContainer = Frame(master)
        self.setimoContainer.pack(pady = 5, padx = 20)

        self.oitavoContainer = Frame(master)
        self.oitavoContainer.pack(pady = 5, padx = 20)


        self.cad = Label(self.primeiroContainer, text = "Cadastro de Clientes")
        self.cad.pack()

        self.buscarID = Label(self.container, text = "Buscar ID:", font = self.fontePadrao)
        self.buscarID.pack(side = LEFT)
        self.entID = Entry(self.container)
        self.entID["width"] = 5
        self.entID.pack(side = LEFT)

        self.botaoID = Button(self.container,text = "Buscar")
        self.botaoID["command"] = self.buscarUsuario
        self.botaoID.pack(padx = 5)
        

        self.txtNome = Label(self.segundoContainer,text = "Nome: ", font = self.fontePadrao, width = 10)
        self.txtNome.pack(side = LEFT)
        self.entNome = Entry(self.segundoContainer)
        self.entNome["width"] = 25
        self.entNome.pack(side = LEFT)

        self.txtTelefone = Label(self.terceiroContainer,text = "Telefone:", font = self.fontePadrao, width = 10)
        self.txtTelefone.pack(side = LEFT)
        self.entTelefone = Entry(self.terceiroContainer)
        self.entTelefone["width"] = 25
        self.entTelefone.pack()

        self.txtEmail = Label(self.quartoContainer,text = "Email:", font = self.fontePadrao, width = 10)
        self.txtEmail.pack(side=LEFT)
        self.entEmail = Entry(self.quartoContainer)
        self.entEmail["width"] = 25
        self.entEmail.pack()

        self.txtEndereco = Label(self.quintoContainer, text = "Endereço:", font = self.fontePadrao, width = 10)
        self.txtEndereco.pack(side = LEFT)
        self.entEndereco = Entry(self.quintoContainer)
        self.entEndereco["width"] =25
        self.entEndereco.pack()

        self.txtCpf = Label(self.sextoContainer, text = "Cpf:", font = self.fontePadrao, width = 10)
        self.txtCpf.pack(side = LEFT)
        self.entCpf = Entry(self.sextoContainer)
        self.entCpf["width"] =25
        self.entCpf.pack()

        self.txtCidade = Label(self.containerComboBox, text = "Cidade:", font = self.fontePadrao, width = 10)
        self.txtCidade.pack(side = LEFT)

        self.combo = ttk.Combobox(self.containerComboBox, values=self.buscarCombo(), state = 'normal')
        self.combo.pack(side = LEFT)

        self.botInsert = Button(self.setimoContainer,text="Inserir", width = 12)
        self.botInsert["command"] = self.inserirCliente
        self.botInsert.pack(side = LEFT)

        self.botAlterar = Button(self.setimoContainer, text = "Alterar", width = 12)
        self.botAlterar["command"] = self.alterarCliente
        self.botAlterar.pack(side = LEFT)

        self.botExcluir = Button(self.setimoContainer,text = "Excluir", width = 12)
        self.botExcluir["command"] = self.excluirCliente
        self.botExcluir.pack(side = LEFT)

        self.botLimpar = Button(self.setimoContainer, text = "Limpar", width = 12)
        self.botLimpar["command"] = self.limpar
        self.botLimpar.pack(side = LEFT)

        self.botPdf = Button(self.setimoContainer, text = "PDF", width = 12, command = self.criarPdf)
        self.botPdf.pack(side = LEFT)

        self.tree = self.createTreeView(master)

    def limpar(self):
        
        if self.entID.get() or self.entNome.get() or self.entTelefone.get() or self.entEmail.get() or self.entEndereco.get() or self.entCpf.get() or self.combo.get():
            self.entID.delete(0, END)
            self.entNome.delete(0, END)
            self.entTelefone.delete(0, END)
            self.entEmail.delete(0, END)
            self.entEndereco.delete(0, END)
            self.entCpf.delete(0, END)
            self.combo.delete(0, END)

            messagebox.showinfo("", "Campos Limpos")
    

    def inserirCliente(self):
        cli = cliente()

        if self.entNome.get() and self.entTelefone.get() and self.entEmail.get() and self.entEndereco.get() and self.entCpf.get() and self.combo.get():
            cli.nome = self.entNome.get()
            cli.telefone = self.entTelefone.get()
            cli.email = self.entEmail.get()
            cli.endereco = self.entEndereco.get()
            cli.cpf = self.entCpf.get()
            cli.cidade = self.combo.get()

            self.entID.delete(0, END)
            self.entNome.delete(0, END)
            self.entTelefone.delete(0, END)
            self.entEmail.delete(0, END)
            self.entEndereco.delete(0, END)
            self.entCpf.delete(0, END)
            self.combo.delete(0, END)

            result = cli.insertCliente()
            messagebox.showinfo("Inserir", result)
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos")

        self.atualizarTreeView()

    def alterarCliente(self):
        cli = cliente()

        if self.entID.get() and self.entNome.get() and self.entTelefone.get() and self.entEmail.get() and self.entEndereco.get() and self.entCpf.get() and self.combo.get():
            cli.id = self.entID.get()
            cli.nome = self.entNome.get()
            cli.telefone = self.entTelefone.get()
            cli.email = self.entEmail.get()
            cli.endereco = self.entEndereco.get()
            cli.cpf = self.entCpf.get()
            cli.cidade = self.combo.get()

            self.entID.delete(0, END)
            self.entNome.delete(0, END)
            self.entTelefone.delete(0, END)
            self.entEmail.delete(0, END)
            self.entEndereco.delete(0, END)
            self.entCpf.delete(0, END)
            self.combo.delete(0, END)

            result = cli.updateCliente()
            messagebox.showinfo("Alterar", result)
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos")
        
        self.atualizarTreeView()

    def excluirCliente(self):
        cli = cliente()

        cli.id = self.entID.get()

        if self.entID.get():
            result = cli.deleteCliente()
            messagebox.showinfo("Deletar", result)

            self.entID.delete(0, END)
            self.entNome.delete(0, END)
            self.entTelefone.delete(0, END)
            self.entEmail.delete(0, END)
            self.entEndereco.delete(0, END)
            self.entCpf.delete(0, END)
            self.combo.delete(0, END)
        else:
            messagebox.showwarning("Aviso", "Selecione um ID para a exclusão")
        
        self.atualizarTreeView()

    def buscarUsuario(self):
        cli = cliente()

        cli.id = self.entID.get()

        if self.entID.get():
            result = cli.selectCliente()
            messagebox.showinfo("Busca", result)

            self.entID.delete(0, END)
            self.entID.insert(INSERT, cli.id)

            self.entNome.delete(0, END)
            self.entNome.insert(INSERT, cli.nome)

            self.entTelefone.delete(0, END)
            self.entTelefone.insert(INSERT,cli.telefone)

            self.entEmail.delete(0, END)
            self.entEmail.insert(INSERT, cli.email)

            self.entEndereco.delete(0, END)
            self.entEndereco.insert(INSERT, cli.endereco)

            self.entCpf.delete(0, END)
            self.entCpf.insert(INSERT, cli.cpf)

            self.combo.delete(0, END)
            self.combo.insert(INSERT, cli.cidade)
        else:
            messagebox.showwarning("Aviso", "Selecione um ID para a busca")
        
    def criarPdf(self):
        cli = cliente()
        dados = cli.buscarTreeView()
        
        c = canvas.Canvas("conteudo_clientes.pdf", pagesize=letter)
        path = "conteudo_clientes.pdf"

        largura, altura = letter
        c.setFont("Helvetica", 10)
        
        x = 100
        y = altura - 50

        c.drawString(x, y, "ID")
        c.drawString(x + 50, y, "Nome")
        c.drawString(x + 150, y, "Telefone")
        c.drawString(x + 230, y, "Email")
        c.drawString(x + 350, y, "Endereço")
        c.drawString(x + 450, y, "CPF")
        c.drawString(x + 550, y, "Cidade")

        y -= 20 

        for linha in dados:
            c.drawString(x, y, str(linha[0]))
            c.drawString(x + 50, y, str(linha[1])) 
            c.drawString(x + 150, y, str(linha[2]))
            c.drawString(x + 230, y, str(linha[3]))
            c.drawString(x + 350, y, str(linha[4]))
            c.drawString(x + 450, y, str(linha[5]))
            c.drawString(x + 550, y, str(linha[6]))
            y -= 15

            if y < 50:
                c.showPage()
                c.setFont("Helvetica", 10)
                y = altura - 50
                c.drawString(x, y, "ID")
                c.drawString(x + 50, y, "Nome")
                c.drawString(x + 150, y, "Telefone")
                c.drawString(x + 230, y, "Email")
                c.drawString(x + 350, y, "Endereço")
                c.drawString(x + 450, y, "CPF")
                c.drawString(x + 550, y, "Cidade")
                y -= 20
        c.save()
        os.startfile(path)


    def createTreeView(self, root):
        
        cli = cliente()

        self.tree = ttk.Treeview(root, columns=("ID", "Nome", "Telefone", "Email", "Endereco", "CPF", "Cidade"), show = "headings")
        self.tree.heading("ID", text = "ID")
        self.tree.heading("Nome", text = "Nome")
        self.tree.heading("Telefone", text = "Telefone")
        self.tree.heading("Email", text = "Email")
        self.tree.heading("Endereco", text = "Endereco")
        self.tree.heading("CPF", text= "CPF")
        self.tree.heading("Cidade", text = "Cidade")
        self.tree.bind("<<TreeviewSelect>>", self.selecionaCliente)
        self.tree.pack(fill = BOTH, expand = True)

        for item in self.tree.get_children():
            self.tree.delete(item)
        rows = cli.buscarTreeView()

        for row in rows:
            self.tree.insert("", END, values=row)
        
        return self.tree
    def atualizarTreeView(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        cli = cliente()
        rows = cli.buscarTreeView()

        for row in rows:
            self.tree.insert("", END, values=row)

    def buscarCombo(self):
        cli = cliente()
        result = cli.buscarComboBox()

        return result
    
    def selecionaCliente(self, event):
        seleciona_item = self.tree.selection()
        if seleciona_item:
            item = seleciona_item[0]
            values = self.tree.item(item, 'values')

            self.entID.delete(0, END)
            self.entID.insert(INSERT, values[0])

            self.entNome.delete(0, END)
            self.entNome.insert(INSERT, values[1])

            self.entTelefone.delete(0, END)
            self.entTelefone.insert(INSERT, values[2])

            self.entEmail.delete(0, END)
            self.entEmail.insert(INSERT, values[3])

            self.entEndereco.delete(0, END)
            self.entEndereco.insert(INSERT, values[4])

            self.entCpf.delete(0, END)
            self.entCpf.insert(INSERT, values[5])

            self.combo.delete(0, END)
            self.combo.insert(INSERT, values[6])
    


if __name__ == "__main__":
    root = Tk()
    root.state('zoomed')
    appClientes(root)
    root.mainloop()

        
