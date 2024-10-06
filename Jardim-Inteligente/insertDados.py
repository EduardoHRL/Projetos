from banco import *

class d():
    
    def busca_dados():
        response = banco.supabase.table('sensor_data').select('horario, umidade_solo').execute()
        if response.data:
            return response.data
        else:
            print("Erro ao buscar dados ou nenhum dado encontrado.")
            return []
        
    

