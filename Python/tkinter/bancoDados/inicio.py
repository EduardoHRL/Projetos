import tkinter as tk
import subprocess

def abrir_janela():

    caminho_py = r"C:\Users\SENAI\AppData\Local\Programs\Python\Python312\python.exe"
    caminho_arquivo = r"C:\Users\SENAI\Documents\ALUNO\aerials\Projetos-Senai\Python\tkinter\bancoDados\aplicativo.py"
    
    subprocess.Popen([caminho_py, caminho_arquivo])

janela = tk.Tk()
botao = tk.Button(janela, text = 'Ir para nova janela', command = abrir_janela)
botao.grid(row = 0, column = 0)

janela.mainloop()