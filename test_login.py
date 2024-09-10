import pytest
import time

from selenium import webdriver

from functions import Functions
from locators import Locators

@pytest.fixture
def setup():
    driver = webdriver.Edge()
    t = 1
    f = Functions(driver)

    return t, f

def test_login(setup):
    t, f = setup
    path = './screenshots'

    # Navegando al sitio herokuapp
    f.navigate('https://the-internet.herokuapp.com/login', t)
    # screenshot del sitio
    f.screenshot(path, '01-heroku-site.png')

    # Enviando el usuario al campo Username
    f.validate_and_send_keys("xpath", Locators.username, "tomsmith", t)
    # screenshot username insertado
    f.screenshot(path, '02-username-insert.png')

    # Enviando el contraseña al campo Password
    f.validate_and_send_keys("xpath", Locators.password, "SuperSecretPassword!", t)
    # screenshot password insertado
    f.screenshot(path, '03-password-insert.png')

    # Dando click al botón login
    f.click("xpath", Locators.login_button, t)
    # screenshot click

    time.sleep(2)
    
    # Validar que el texto Welcome to the Secure Area. When you are done click 
    # logout below. este en la pagina
    if f.validate_element("xpath", Locators.check):
        print("Login Correcto")
        f.screenshot(path, '04-correct-login.png')

