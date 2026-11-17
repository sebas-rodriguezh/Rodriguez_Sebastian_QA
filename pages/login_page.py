from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:
    """Page Object de la pantalla de inicio de sesión de ShopGo."""
    
    # Locators
    INPUT_EMAIL = (AppiumBy.ACCESSIBILITY_ID, "input_email")
    INPUT_PASSWORD = (AppiumBy.ACCESSIBILITY_ID, "input_password")
    BTN_LOGIN = (AppiumBy.ACCESSIBILITY_ID, "btn_login")
    TXT_ERROR = (AppiumBy.ACCESSIBILITY_ID, "txt_error")
    HOME_TITLE = (AppiumBy.ACCESSIBILITY_ID, "home_title")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def _esperarv_isible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def ingresar_correo(self, correo):
        campo = self._esperar_visible(self.INPUT_EMAIL)
        campo.clear()
        campo.send_keys(correo)

    def ingresar_password(self, password):
        campo = self._esperar_visible(self.INPUT_PASSWORD)
        campo.clear()
        campo.send_keys(password)

    def tocar_iniciar_sesion(self):
        self.wait.until(EC.element_to_be_clickable(self.BTN_LOGIN)).click()

    def iniciar_sesion(self, correo, password):
        self.ingresar_correo(correo)
        self.ingresar_password(password)
        self.tocar_iniciar_sesion() 

    def obtener_mensaje_error(self):
        return self._esperar_visible(self.TXT_ERROR).text

    def obtener_titulo_home(self):
        return self._esperar_visible(self.HOME_TITLE).text  