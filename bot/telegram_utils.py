import requests

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