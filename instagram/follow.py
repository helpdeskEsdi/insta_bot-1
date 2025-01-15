import time
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bot.telegram_utils import send_profile_followed

def follow_users(driver, token, chat_id):
    follows_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../follows.xlsx')

    df = pd.read_excel(follows_path, header=None)

    # Opciones del navegador
    options = Options()
    options.add_argument("--start-maximized")  # Inicia maximizado
    options.add_argument("--disable-notifications")  # Deshabilita notificaciones
    options.add_argument("--disable-popup-blocking")  # Evita bloqueos de popups

    driver = webdriver.Chrome(options=options)

    # Crear la carpeta de capturas si no existe
    screenshot_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../screenshots')
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    for followed in df.iloc[:, 0]:
        url_perfil = f"https://www.instagram.com/{followed.strip()}"
        print(f"Accediendo al perfil: {url_perfil}")
        
        try:
            driver.get(url_perfil)

            # Esperar a que el perfil se cargue
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[text()='Publicaciones']"))
            )

            # Revisar si ya estamos siguiendo al usuario
            try:
                follow_btn = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Seguir')]"))
                )
                follow_btn.click()
                print(f"Se siguió a: {followed}")

                # Crear un nombre único para la captura
                screenshot_path = os.path.join(screenshot_dir, f"{followed.strip()}_followed.png")
                driver.get_screenshot_as_file(screenshot_path)

                # Enviar la captura de pantalla al bot de Telegram
                send_profile_followed(bot_token, bot_chatID, screenshot_path)
                print("Captura de pantalla enviada exitosamente.")
            except Exception as e:
                print(f"No se encontró el botón 'Seguir' en el perfil de {followed}. Puede que ya lo sigas o sea un perfil privado. Error: {e}")
            
            # Esperar un poco antes de continuar con el siguiente perfil
            time.sleep(5)
        
        except Exception as e:
            print(f"Error al acceder al perfil de {followed}: {e}")
            continue

    driver.quit()
