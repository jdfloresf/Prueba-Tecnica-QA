import os

from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Functions:
    def __init__(self, driver:webdriver):
        """Inicializa una instancia de la clase WebAutomation.
        Args:
            driver (webdriver): WebDriver de Selenium
        """
        self.driver = driver

    def wait(self, t:int):
        """Espera una cantidad de tiempo especificada.

        Args:
            t (int): Tiempo en segundos para esperar.
        """
        self.driver.implicitly_wait(t)

    def navigate(self, Url:str, t:int):
        """Navega a una URL especificada y maximiza la ventana del navegador.

        Args:
            Url (string): URL a la que se va a navegar
            t (int): Tiempo en segundos para esperar después de navegar.
        """
        self.driver.get(Url)
        print(f"Navegando a: {Url}")
        self.driver.maximize_window()
        self.wait(t)

    def validate_element(self, locator_type:str, locator:str) -> WebElement:
        """ Valida la presencia de un elemento en la página usando un localizador, 
        lo desplaza a la vista,lo limpia y envía un texto al campo del elemento.

        Args:
            locator_type (string): Tipo de localizador (xpath o id)
            locator (string):  El localizador del elemento
            text (string): Texto a enviar al campo del elemento.
            t (int): Tiempo en segundos para esperar después de interactuar con 
            el elemento.
        """
        locator_dict = {
            "xpath": By.XPATH,
            "id": By.ID,
        }

        try:
            if locator_type in locator_dict:
                by_type = locator_dict[locator_type]
                val = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((by_type, locator)))
                self.driver.execute_script("arguments[0].scrollIntoView();", val)
                return self.driver.find_element(by_type, locator)

            else:
                raise ValueError(f"Tipo de selector no soportado: {locator_type}")
            
        except TimeoutException as ex:
            print(ex.msg)
            print(f"\nNo se encontro elemento: {locator}")
            return None

    def validate_and_send_keys(self, locator_type:str, locator:str, 
                                          text:str, t:int):
        """ Valida la presencia de un elemento en la página usando un selector, 
        lo desplaza a la vista,lo limpia y envía un texto al campo del elemento.

        Args:
            locator_type (string): Tipo de localizador (xpath o css)
            locator (string):  El localizador del elemento
            text (string): Texto a enviar al campo del elemento.
            t (int): Tiempo en segundos para esperar después de interactuar con 
            el elemento.
        """
        try:
            element = self.validate_element(locator_type, locator)
            if element:
                element.clear()
                element.send_keys(text)
                self.wait(t)
                print(f"Rellenando campo {locator} con -> {text}")
        except TimeoutException as ex:
            print(ex.msg)
            print(f"\nNo se encontro elemento: {locator}")

    def click(self, locator_type:str, locator:str, t:int):
        """Hace click en un elemento de la página usando un selector y desplaza 
            el elemento a la vista.

        Args:
            locator_type (string): Tipo de localizador (xpath o css)
            locator (string): El localizador del elemento.
            t (int): Tiempo en segundos para esperar después de hacer clic en 
            el elemento.
        """
        try:
            element = self.validate_element(locator_type, locator)
            if element:
                element.click()
                print(f"\nDando click en campo: {locator}")
                self.wait(t)
        
        except TimeoutException as ex:
            print(ex.msg)
            print(f"\nNo se puede dar click en elemento: {locator}")

    def screenshot(self, path, file_name):
        """Toma una captura de pantalla y la guarda en la ruta especificada

        Args:
            path (str): ruta donde se guardará la captura
            sc_name (str): nombre de la captura con extensión .png
        """
        if not os.path.exists(path):
            os.makedirs(path)
        self.driver.save_screenshot(os.path.join(path, file_name))

    def tearDown(self, t: int):
        """Realiza acciones de limpieza después de la ejecución de los tests.
           Espera un tiempo especificado antes de cerrar el navegador.
        """
        self.wait(t)
        self.driver.close()
