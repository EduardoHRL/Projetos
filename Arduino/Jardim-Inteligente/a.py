import requests
import customtkinter as ctk

esp32_ip = "http://192.168.100.200"

def ligar_rele():
    try:
        response = requests.get(f"{esp32_ip}/rele/on")
        if response.status_code == 200:
            status_label.configure(text="Irrigação ligado")
            controle_label.configure(text="Irrigação manual ativada")
        else:
            status_label.configure(text="Erro ao ligar a irrigação")
    except requests.exceptions.RequestException as e:
        status_label.configure(text=f"Erro: {e}")

def desligar_rele():
    try:
        response = requests.get(f"{esp32_ip}/rele/off")
        if response.status_code == 200:
            status_label.configure(text="Irigação desligada")
            controle_label.configure(text="Irrigação manual ativada")
        else:
            status_label.configure(text="Erro ao desligar a irrigação")
    except requests.exceptions.RequestException as e:
        status_label.configure(text=f"Erro: {e}")

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
    except requests.exceptions.RequestException as e:
        temperatura_label.configure(text=f"Erro: {e}")
        umidade_solo_label.configure(text=f"Erro: {e}")
        umidade_ar_label.configure(text=f"Erro: {e}")

def desativar_controle_manual():
    try:
        response = requests.get(f"{esp32_ip}/set_controle_manual?manual=off")
        if response.status_code == 200:
            controle_label.configure(text="Irrigação manual desativada")
            status_label.configure(text="Status da irrigação")
        else:
            controle_label.configure(text="Erro ao desativar irrigação manual")
    except requests.exceptions.RequestException as e:
        controle_label.configure(text=f"Erro: {e}")

root = ctk.CTk()
root.geometry("400x400")
root.resizable(width= False, height= False)
root.title("Jardim Inteligente ESP32")

aba1 = ctk.CTkTabview(root)
aba1.pack(fill="both", expand=True)

tab_rele = aba1.add("Controle do Relé")

ligar_button = ctk.CTkButton(tab_rele, text="Irrigar", command=ligar_rele)
ligar_button.pack(pady=10)

desligar_button = ctk.CTkButton(tab_rele, text="Desligar irrigação", command=desligar_rele)
desligar_button.pack(pady=10)

controle_manual_off_btn = ctk.CTkButton(tab_rele, text="Ligar irrigação Automatica", command=desativar_controle_manual)
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

root.mainloop()
