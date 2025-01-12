from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from instagram.login import load_cookies
from bot.telegram_utils import send_profile_image  

def go_profile(driver, bot_token, bot_chatID):
    
    try:

        profile_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Perfil']"))
        )
        profile_btn.click()
        print("Has accedido al perfil.")


        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Publicaciones']"))
        )
        print("La página de perfil se ha cargado correctamente.")

        # Tomar la captura de pantalla
        screenshot_path = '../screenshots/profile.png'
        driver.get_screenshot_as_file(screenshot_path)

        # Enviar la captura de pantalla al bot de Telegram
        send_profile_image(bot_token, bot_chatID, screenshot_path)
        print("Captura de pantalla enviada exitosamente.")

    except Exception as e:
        print(f"No se pudo acceder al perfil o enviar la captura: {e}")

