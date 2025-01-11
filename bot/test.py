import requests

token = '7614189700:AAGZV6cnbtRGmOChSF4txBajQ61KfWjVUfY'
chat_id = '8024601173'
message = "Funciona!!!"

def send_test_message(token, chat_id, message, parse_mode='Markdown'):

    # URL base para la API de Telegram
    url = f'https://api.telegram.org/bot{token}/sendMessage'

    # Parámetros que se pasan en la solicitud GET
    params = {
        'chat_id': chat_id,
        'parse_mode': parse_mode,
        'text': message
    }

    try:
        # Realizar la solicitud GET con los parámetros
        response = requests.get(url, params=params)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            print("Mensaje enviado exitosamente.")
        else:
            print(f"Error: No se pudo enviar el mensaje. Código de estado: {response.status_code}")
        
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return None
 
send_test_message(token=token, chat_id=chat_id, message=message, parse_mode='Markdown')