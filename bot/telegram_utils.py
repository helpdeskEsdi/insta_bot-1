import requests

def send_profile_image(token, bot_chatID, screenshot_path):
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    
    with open(screenshot_path, 'rb') as photo:
        response = requests.post(url, data={'chat_id': bot_chatID}, message={'text:'"Foto del perfil"}, files={'photo': photo})
    return response