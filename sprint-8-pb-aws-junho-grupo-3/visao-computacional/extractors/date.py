from datetime import datetime
import pytz

def format_date():
    # Define o fuso horário
    timezone = pytz.timezone('America/Sao_Paulo')
    # Obtém o horário atual
    time = datetime.now()
    # Converte o horário atual para o fuso horário desejado
    local_time = time.astimezone(timezone)

    return local_time.strftime("%d-%m-%Y %H:%M:%S")