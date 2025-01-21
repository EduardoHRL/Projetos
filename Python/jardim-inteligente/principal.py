import requests
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from insertDados import d
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates
from datetime import datetime
from tkcalendar import DateEntry
import sys

esp32_ip = "http://192.168.200.44"


def ligar_irrigacao():
    try:
        response = requests.get(f"{esp32_ip}/rele/on")
        if response.status_code == 200:
            status_label.configure(text="Irrigação ligada")
            controle_label.configure(text="Irrigação manual ativada")
        else:
            status_label.configure(text="Erro ao ligar a irrigação")
    except:
        status_label.configure(text=f"Erro ao ligar a irrigação")

def desligar_irrigacao():
    try:
        response = requests.get(f"{esp32_ip}/rele/off")
        if response.status_code == 200:
            status_label.configure(text="Irrigação desligada")
            controle_label.configure(text="Irrigação manual ativada")
        else:
            status_label.configure(text="Erro ao desligar a irrigação")
    except:
        status_label.configure(text=f"Erro ao desligar a irrigação")

def atualizar_dados():
    try:
        response = requests.get(f"{esp32_ip}/get_sensores")
        if response.status_code == 200:
            dados = response.json()
            temperatura_label.configure(text=f"Temperatura: {dados['temperatura']}°C")
            umidade_solo_label.configure(text=f"Umidade do Solo: {dados['umidade_solo']}%")
            umidade_ar_label.configure(text=f"Umidade do Ar: {dados['umidade_ar']}%")
        else:
            temperatura_label.configure(text="Erro ao obter temperatura")
            umidade_solo_label.configure(text="Erro ao obter umidade do solo")
            umidade_ar_label.configure(text="Erro ao obter umidade do ar")
    except:
        temperatura_label.configure(text=f"Erro ao obter temperatura")
        umidade_solo_label.configure(text=f"Erro ao obter umidade do solo")
        umidade_ar_label.configure(text=f"Erro ao obter umidade do ar")

def ligar_irrigacao_automatica():
    try:
        response = requests.get(f"{esp32_ip}/set_controle_manual?manual=off")
        if response.status_code == 200:
            controle_label.configure(text="Irrigação automatica ativada")
            status_label.configure(text="Status da irrigação")
        else:
            controle_label.configure(text="Erro ao ativar irrigação automatica")
            status_label.configure(text="Status da irrigação")
    except:
        controle_label.configure(text=f"Erro ao ativar irrigação automatica")
        status_label.configure(text=f"Status da irrigação")

def gerar_grafico_por_data(parent, data_selecionada, canvas_frame):
    dados = d.busca_dados()

    for widget in canvas_frame.winfo_children():
        widget.destroy()

    data_filtrada = datetime.strptime(data_selecionada, '%d/%m/%Y').date()
    dados_filtrados = []

    for dado in dados:
        horario = dado.get('horario')
        if horario is not None:
            try:
                if datetime.strptime(horario, '%Y-%m-%dT%H:%M:%S').date() == data_filtrada:
                    dados_filtrados.append(dado)
            except ValueError:
                print(f"Formato de data inválido: {horario}")

    if not dados_filtrados:
        messagebox.showinfo("Aviso",  f"Sem dados para a data: {data_selecionada}")
        return

    horarios = [datetime.strptime(dado['horario'], '%Y-%m-%dT%H:%M:%S') for dado in dados_filtrados]
    temperaturas = [dado['temperatura'] for dado in dados_filtrados]
    umidades_solo = [dado['umidade_solo'] for dado in dados_filtrados]
    umidades_ar = [dado['umidade_ar'] for dado in dados_filtrados]

    fig, ax = plt.subplots(figsize=(8, 6))

    # Plotando as informações filtradas
    ax.plot(horarios, temperaturas, label='Temperatura (°C)', color='red', marker='o')
    ax.plot(horarios, umidades_solo, label='Umidade do Solo (%)', color='blue', marker='o')
    ax.plot(horarios, umidades_ar, label='Umidade do Ar (%)', color='green', marker='o')

    ax.set_xlabel('Hora')
    ax.set_ylabel('Valores')
    ax.set_title(f'Dados do Sensor para {data_selecionada}')
    ax.legend()
    ax.grid(True)

    # Configurando o eixo X
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    fig.tight_layout()

    # Exibir o gráfico no tkinter
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=BOTH, expand=True)

    canvas_frame.pack(fill=BOTH, expand=True)

def grafico(parent):

    def gerar_grafico():
        data_selecionada = date_entry.get_date().strftime('%d/%m/%Y')
        for widget in canvas_frame.winfo_children():
            widget.destroy()
        gerar_grafico_por_data(parent, data_selecionada, canvas_frame)

    date_label = ctk.CTkLabel(parent, text="Selecione a Data:")
    date_label.pack(pady=10)

    date_entry = DateEntry(parent, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')  # DateEntry com formato dd/mm/yyyy
    date_entry.pack(pady=10)

    botao_gerar_grafico = ctk.CTkButton(parent, text="Gerar Gráfico", command=gerar_grafico)
    botao_gerar_grafico.pack(pady=10)

    canvas_frame = Frame(parent)
    canvas_frame.pack(fill=BOTH, expand=True)

root = ctk.CTk()
root.title("Jardim Inteligente ESP32")

aba1 = ctk.CTkTabview(root)
aba1.pack(fill="both", expand=True)

tab_rele = aba1.add("Controle da irrigação")

ligar_button = ctk.CTkButton(tab_rele, text="Irrigar", command=ligar_irrigacao)
ligar_button.pack(pady=10)

desligar_button = ctk.CTkButton(tab_rele, text="Desligar irrigação", command=desligar_irrigacao)
desligar_button.pack(pady=10)

controle_manual_off_btn = ctk.CTkButton(tab_rele, text="Ligar irrigação Automática", command=ligar_irrigacao_automatica)
controle_manual_off_btn.pack(pady=10)

status_label = ctk.CTkLabel(tab_rele, text="Status da irrigação")
status_label.pack(pady=10)

controle_label = ctk.CTkLabel(tab_rele, text="")
controle_label.pack(pady=5)

abaSensores = aba1.add("Dados dos Sensores")

atualizar_button = ctk.CTkButton(abaSensores, text="Atualizar Dados", command=atualizar_dados)
atualizar_button.pack(pady=10)

temperatura_label = ctk.CTkLabel(abaSensores, text="Temperatura: --°C")
temperatura_label.pack(pady=5)

umidade_solo_label = ctk.CTkLabel(abaSensores, text="Umidade do Solo: --%")
umidade_solo_label.pack(pady=5)

umidade_ar_label = ctk.CTkLabel(abaSensores, text="Umidade do Ar: --%")
umidade_ar_label.pack(pady=5)

abaDados = aba1.add("Dados por Hora")
grafico(abaDados)

root.mainloop()

sys.exit()