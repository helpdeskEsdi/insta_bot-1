import json
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


def open_login():
   
    # Opciones del navegador
    options = Options()
    options.add_argument("--start-maximized")  # Inicia maximizado

    # Inicializar el controlador de Chrome
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)

    try:
        cookies_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Permitir todas las cookies')]")
        cookies_btn.click()
        time.sleep(3)
    except:
        print("El botón de cookies no se encontró o ya se había hecho clic antes.")

    # Mantener la sesión abierta para usarla más tarde
    return driver



def load_cookies(driver, cookies_file="../cookies.json", use_json=True):

    open_login()

    if use_json:
        with open(cookies_file, "r") as cookie_file:
            cookies = json.load(cookie_file)
    else:
        with open(cookies_file, "rb") as cookie_file:
            cookies = pickle.load(cookie_file)

    # Agregar las cookies a la sesión de Selenium
    for cookie in cookies:
    
        if 'domain' in cookie:
            del cookie['domain']

            if 'sameSite' not in cookie or cookie['sameSite'] not in ["Strict", "Lax", "None" ]:
                cookie['sameSite'] = "Lax"
        
        try: 
            driver.add_cookie(cookie)
        except Exception as e: 
            print(f"Error al agregar cookie {e}")
        
    else: 
        print(f"Cookie omitida por falta de 'name o 'value': ")

    driver.refresh()
    
    time.sleep(5)

