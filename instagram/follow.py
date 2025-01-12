import time
from bot.telegram_utils import send_profile_followed
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def follow_users(driver, bot_token, bot_chatID):

    # Leer el archivo Excel
    df = pd.read_excel('../follows.xlsx', header=None)

    # Opciones del navegador
    options = Options()
    options.add_argument("--start-maximized")  # Inicia maximizado
    options.add_argument("--disable-notifications")  # Deshabilita notificaciones
    options.add_argument("--disable-popup-blocking")  # Evita bloqueos de popups

    driver = webdriver.Chrome(options=options)

    for followed in df.iloc[:, 0]:
        url_perfil = f"https://www.instagram.com/{followed.strip()}"
        print(f"Accediendo al perfil: {url_perfil}")
        
        try:
            driver.get(url_perfil)
            
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[text()='Publicaciones']"))
            )

            try:
                follow_btn = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Seguir')]"))
                )
                follow_btn.click()
                print(f"Se siguió a: {followed}")

                screenshot_path = '../screenshots/followed.png'
                driver.get_screenshot_as_file(screenshot_path)

                send_profile_followed(bot_token, bot_chatID, screenshot_path)
                print("Captura de pantalla enviada exitosamente.")

            except:
                print(f"No se encontró el botón 'Seguir' en el perfil de {followed}. Puede que ya lo sigas o sea un perfil privado.")
            
            time.sleep(5)
        
        except Exception as e:
            print(f"Error al acceder al perfil de {followed}: {e}")
            continue

    driver.quit()
