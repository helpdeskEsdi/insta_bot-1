from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def go_profile(driver):
    
    try: 
        profile_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Perfil']"))
        )
        profile_btn.click()
        print("Has accedido al perfil.")

        # Esperar a que cargue la página del perfil
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[text()='Publicaciones']"))
        )
        print("La página de perfil se ha cargado correctamente.")
        
    except Exception as e:
        print(f"No se pudo acceder al perfil: {e}")