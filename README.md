# Prueba técnica - QA Automation Mobile (ShopGo)

Solución de Sebastián Rodríguez Hernández a la prueba técnica de la pasantía de QA Automation Mobile.

## Requisitos
- Python 3.10 o superior (desarrollado con Python 3.13)

## Estructura
| Archivo | Contenido |
|---|---|
| `parte1_casos/casos_login.md` | Parte 1: casos de prueba del inicio de sesión |
| `shopgo/validaciones.py` | Parte 2: `validar_password` y `calcular_envio` |
| `tests/test_validaciones.py` | Parte 2: pruebas con pytest |
| `pages/login_page.py` | Parte 3: Page Object de la pantalla de login |
| `tests/conftest.py` | Parte 3: fixture del driver de Appium |
| `tests/test_login.py` | Parte 3: pruebas de UI de login |
| `parte4_bug/reporte_bug.md` | Parte 4: reporte de bug |
| `NOTAS.md` | Suposiciones, uso de IA y tiempo invertido |

## Instalación

**Windows (PowerShell)**
```
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
Si PowerShell bloquea la activación, ejecutar una vez:
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

**macOS / Linux**
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecutar las pruebas (Parte 2)
```
pytest tests/test_validaciones.py
```
Para ver cada prueba por nombre: `pytest tests/test_validaciones.py -v`

## Sobre la Parte 3 (UI mobile)
Las pruebas de `tests/test_login.py` no se ejecutan en este entorno, porque requieren
Appium Server, un emulador o dispositivo y el APK de ShopGo. Para verificar que están
bien escritas y que pytest las encuentra:
```
pytest tests/test_login.py --collect-only
```
Para ejecutarlas en un entorno real: levantar Appium en `http://127.0.0.1:4723` y
ajustar las capabilities de ejemplo en `tests/conftest.py` (dispositivo y ruta del APK).

> Ejecutar solo `pytest`, sin indicar el archivo, también intenta correr `test_login.py`,
> que falla al no encontrar el servidor de Appium. Por eso se indica el archivo.