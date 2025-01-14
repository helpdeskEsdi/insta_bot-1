import datetime as dt
import pandas as pd
import os

def generate_report():
    
    #Nombre del usuario
    username = "x_esdi"
    path = f"../reports/{username}_followers.xlsx"

    #Crear excel
    writer = pd.ExcelWriter(f"{path}", engine="xlsxwriter")
    df.to_excel(writer, sheet_name="Seguimiento de seguidores")

    data = [
        ["Total Followers", "New followers", "Unfollows", "Date"]
    ]
    for row in data:
        sheet.append(row)
    
    wb.save(f"../reports/{username}_followers.xlsx")
    print("Excel creado con exito")




   

    try:
        os.path.exists("../reports")
        print("Si existe la carpeta")
    except Exception as e:
        print("No existe la carpeta para almacenar los reports")
    


def get_date():
     #Cojer fecha actual
    date = dt.datetime.now().strftime("%d-%m-%Y %H:%M")
    print(date)


generate_report()