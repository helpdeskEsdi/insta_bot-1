import requests
import os
#Adjuntar texto junto a la imagen: -F caption="<TEXTO JUNTO IMAGEN>"

#Envia foto del perfil de nuestro usuario
def send_profile_image(token, bot_chatID, screenshot_path):
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    
    with open(screenshot_path, 'rb') as photo:
        response = requests.post(url, data={'chat_id': bot_chatID}, files={'photo': photo})
    return response


#Enviar foto de cuenta seguida
def send_profile_followed(token, bot_chatID, screenshot_path):
    url = f'https://api.telegram.org/bot{token}/sendPhoto'

    with open(screenshot_path, 'rb') as photo: 
        response = requests.post(url, data={'chat_id': bot_chatID}, files={'photo': photo})
    return response


#Envia el excel con el seguimiento de seguidores
import requests

def send_followers(token, bot_chatID, total_followers, new_followers, unfollows):
    url = f'https://api.telegram.org/bot{token}/sendMessage'

    # Crear el mensaje
    message = f"📊 **Seguidores Report**\n\n"
    message += f"**Seguidores actuales:** {total_followers}\n"
    message += f"**Seguidores nuevos:** {new_followers}\n"
    message += f"**Seguidores perdidos:** {unfollows}"

    # Datos a enviar
    payload = {
        'chat_id': bot_chatID,
        'text': message,
        'parse_mode': 'Markdown'
    }

    try:
        # Enviar la solicitud POST con los datos
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Mensaje enviado a Telegram con éxito.")
        else:
            print(f"Error al enviar mensaje a Telegram: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error al conectar con la API de Telegram: {e}")



def send_followers_report(token, chat_id):
    
    url = f'https://api.telegram.org/bot{token}/sendDocument'

    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../report_x_esdi_followers.xlsx')
    
    try:

        with open(file_path, 'rb') as file:
            response = requests.post(url, data={'chat_id': chat_id}, files={'document': file})

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            print("Mensaje enviado exitosamente.")
        else:
            print(f"Error: No se pudo enviar el mensaje. Código de estado: {response.status_code}")
        
        return response
    
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return None


    

