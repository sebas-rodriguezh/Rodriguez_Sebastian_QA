from pages.login_page import LoginPage

def test_login_exitoso_muestra_titulo_bienvenida(driver):
    login_page = LoginPage(driver)
    login_page.iniciar_sesion("sebas@shopgo.com", "Sebas0812")
    assert login_page.obtener_titulo_home() == "Bienvenido"

def test_login_fallido_muestra_mensaje_de_error(driver):
    login = LoginPage(driver)
    login.iniciar_sesion("sebas@shopgo.com", "Sebas0000")
    assert login.obtener_mensaje_error() == "Correo o contraseña incorrectos"