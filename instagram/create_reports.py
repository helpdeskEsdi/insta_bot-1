import os
import pandas as pd
import datetime as dt
from bot.telegram_utils import send_followers

token = '7614189700:AAGZV6cnbtRGmOChSF4txBajQ61KfWjVUfY'
bot_chatID = '8024601173'


def create_report(num_followers):
    username = "x_esdi"
    
    # Encabezados del excel
    data = [
        ["Total Followers", "New followers", "Unfollows", "Date"]
    ]
    
    # Inicializamos "New followers" y "Unfollows" como 0
    new_followers = 0
    unfollows = 0
    
    # Fecha actual
    date = dt.datetime.now().strftime("%d-%m-%Y %H:%M")

    # Creamos un DataFrame con los encabezados
    df = pd.DataFrame(data[1:], columns=data[0])
    
    # Ruta al archivo de Excel
    file_path = f'report_{username}_followers.xlsx'

    # Si el archivo no existe, lo creamos
    if not os.path.exists(file_path):
        try:
            # Crear el archivo Excel con los encabezados
            with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
                df.to_excel(writer, index=False, sheet_name="Seguidores")
            print(f"Archivo Excel creado: {file_path}")
        
        except Exception as e:
            print(f"Error al crear el archivo Excel: {str(e)}")
            return

    try:
        # Leer el archivo Excel si existe
        df_existing = pd.read_excel(file_path, engine="openpyxl", sheet_name="Seguidores")
        
        # Comprobamos si el DataFrame está vacío
        if df_existing.empty:
            print("El archivo está vacío, no se puede obtener el último número de seguidores.")
            last_followers = 0  # Asumimos que no hay datos previos, por lo que no se calcula "seguidores nuevos"
        else:
            # Obtenemos el último número de seguidores registrado
            last_followers = df_existing["Total Followers"].iloc[-1]
            print(f"Último número de seguidores registrado: {last_followers}")
        
            # Calcular los seguidores nuevos
            new_followers = num_followers - last_followers if num_followers > last_followers else 0
            unfollows = num_followers - last_followers if num_followers < last_followers else 0 
            print(f"Seguidores nuevos: {new_followers}")
            print(f'Seguidores perdidos: {unfollows}')
    
    except Exception as e:
        print(f"Error al leer el archivo Excel: {str(e)}")
        return
    
    # Añadir los datos actuales al DataFrame
    new_data = {
        "Total Followers": num_followers,
        "New followers": new_followers,
        "Unfollows": unfollows,  # Aquí puedes agregar la lógica para calcular "Unfollows"
        "Date": date
    }
    
    # Si el archivo ya existe y tiene datos, añadimos la nueva fila, de lo contrario, usamos el DataFrame original
    if os.path.exists(file_path) and not df_existing.empty:
        df_existing = pd.concat([df_existing, pd.DataFrame([new_data], columns=df.columns)], ignore_index=True)
    else:
        df_existing = pd.DataFrame([new_data], columns=df.columns)
    
    # Guardamos los datos en el archivo Excel
    try:
        with pd.ExcelWriter(file_path, engine="openpyxl", mode="w") as writer:
            df_existing.to_excel(writer, index=False, sheet_name="Seguidores")
            print("Datos guardados en Excel correctamente.")
    
    except Exception as e:
        print(f"Error al guardar en Excel: {str(e)}")

    send_followers(token, bot_chatID, num_followers, last_followers, unfollows)
