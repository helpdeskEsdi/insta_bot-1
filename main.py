from instagram.login import open_login, load_cookies
from instagram.profiles import go_profile #get_followers
from instagram.follow import follow_users

bot_token = '7614189700:AAGZV6cnbtRGmOChSF4txBajQ61KfWjVUfY'
bot_chatId = '8024601173'


if __name__ == "__main__":
    # Iniciar sesión en Instagram (abre el navegador)
    driver = open_login()

    # Cargar las cookies si están disponibles
    load_cookies(driver, cookies_file="cookies.json", use_json=True)

    # Acceder al perfil y tomar la captura de pantalla
    go_profile(driver, bot_token, bot_chatId)
    
    #get_followers(driver)
    
    follow_users(driver, bot_token, bot_chatId)

    # Cerrar el navegador después de completar el proceso
    driver.quit()
