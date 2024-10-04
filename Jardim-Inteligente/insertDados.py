from banco import *

class d():
    
    def buscaTemperatura():
        response = banco.supabase.table('sensor_data').select('temperatura').execute()
        data = response.data

        rows = []
        for record in data:
            valor = list(record.values())
            rows.append(valor)

        return rows
    
    def busca_dados():
        response = banco.supabase.table('sensor_data').select('horario, temperatura, umidade_solo, umidade_ar').execute()
        if response.data:  # Verificando se há dados na resposta
            return response.data
        else:
            print("Erro ao buscar dados ou nenhum dado encontrado.")
            return []
        
    

