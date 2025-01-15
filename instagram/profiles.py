from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from instagram.login import load_cookies
from bot.telegram_utils import send_profile_image  
from instagram.create_reports import create_report
import re

########################################################
######### Accede al perfil y envia una captura #########
########################################################

def go_profile(driver, token, chat_id):
    
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

        # Obtener la ruta absoluta del directorio actual
        current_dir = os.path.dirname(os.path.abspath(__file__))
        screenshot_dir = os.path.join(current_dir, '../screenshots')

        # Verificar si la carpeta 'screenshots' existe, si no, crearla
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
            print(f"Carpeta '{screenshot_dir}' creada.")

        # Ruta para la captura de pantalla
        screenshot_path = os.path.join(screenshot_dir, 'profile.png')

        driver.get_screenshot_as_file(screenshot_path)

        # Enviar la captura de pantalla al bot de Telegram
        send_profile_image(token, chat_id, screenshot_path)
        
        print("Captura de pantalla enviada exitosamente.")

    except Exception as e:
        print(f"No se pudo acceder al perfil o enviar la captura: {e}")


########################################################
## Recoge el numero de seguidores que tiene la cuenta ##
########################################################

def get_num_followers(driver):

    try:

        profile_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Perfil']"))
        )
        profile_btn.click()
        print("Ha accedido al perfil.")


        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Publicaciones']"))
        )
        print("La página de perfil se ha cargado correctamente.")


        followers_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "/followers/")]'))
        )
        
        num_followers_txt = (followers_link.text)
        
        num_followers = int(re.sub(r'\D', '', num_followers_txt))
        
        print(f"El número de seguidores es: {num_followers}") # Reemplaza todo lo que no sea un número con ''
        create_report(num_followers)

    except Exception as e: 
        print("No se ha podido extraer los seguidores")
        print(f"Error: {e}")
