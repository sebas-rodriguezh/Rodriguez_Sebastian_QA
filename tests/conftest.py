import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

APPIUM_SERVER_URL = "http://127.0.0.1:4723"

@pytest.fixture
def driver():
    """Abre la app antes de cada prueba y la cierra al terminar."""
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "Android Emulator"  
    options.app = "C:/ruta/a/ShopGo.apk"

    driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
    yield driver
    driver.quit()