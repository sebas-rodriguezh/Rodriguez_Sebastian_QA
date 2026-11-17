# Notas

## Tiempo invertido
- Total aproximado: 2 horas, 30 minutos, incluida la instalación del entorno desde cero
  (VS Code, entorno virtual y dependencias).

## Suposiciones

### Parte 1 - Casos de prueba
- El PDF solo define el mensaje "Correo o contraseña incorrectos". Para correo con formato
  inválido, campos vacíos y contraseñas que no cumplen las reglas, supuse que la app
  muestra un mensaje de error y no inicia sesión.
- Para un usuario no registrado se muestra el mismo mensaje genérico, para no revelar qué
  correos existen.
- No se define el mensaje de bloqueo. Supuse un aviso claro y que durante los 5 minutos
  ni la contraseña correcta permite entrar.
- Sin conexión: supuse un aviso de falta de conexión que no cuenta como intento fallido.
- TC-09 usa una cuenta distinta para cada variante, para no activar el bloqueo de 3 intentos.

### Parte 2 - Validaciones
- Se permiten caracteres especiales en la contraseña (el PDF no los prohíbe).
- No se exige minúscula (el PDF no la pide).
- "Ningún espacio" aplica a cualquier posición, incluidos el inicio y el final.
- `validar_password(None)` devuelve `False` en lugar de lanzar un error.
- Un subtotal de 0 es válido y paga envío (₡2 500). Solo los negativos lanzan `ValueError`.
- Agregué `pytest.ini` con `pythonpath = .` para que las pruebas puedan importar `shopgo`
  al ejecutar `pytest tests/test_validaciones.py` desde la raíz.

### Parte 3 - UI mobile
- Se asume que existe la cuenta de prueba `sebas@shopgo.com` / `Sebas0812` en el ambiente de QA.
- Las capabilities son de ejemplo (Android, UiAutomator2, emulador, ruta ficticia al APK).
- `home_title` pertenece a la pantalla principal. Lo dejé en `LoginPage` para respetar la
  estructura pedida; en un proyecto más grande iría en una clase `HomePage`.

### Parte 4 - Reporte de bug
- Faltaban datos (modelo, versión de la app, frecuencia). Los dejé como preguntas abiertas
  en lugar de suponerlos.

## Uso de IA

**Herramienta:** Claude (Anthropic), usado como tutor, antes de escribir cada parte me
explicaba los conceptos, y yo revisaba, preguntaba y ajustaba.

### Parte 1 - Casos de prueba
- IA: propuesta inicial de casos y explicación de la técnica de valores límite.
- Yo: agregué el caso de usuario no registrado (TC-03) y el de correo sin nombre antes del
  @ (TC-08), combiné los límites inválidos (7 y 21) en un solo caso y definí los datos de prueba. Al final, tomé los casos supuestos por la IA, para poder manualmente ajustarlos y revisar si aplicaban correctamente para la prueba. 

### Parte 2 - Validaciones y pruebas 

- IA: Idea del formato de `validaciones.py` y explicación de `parametrize`, `ids` y `pytest.raises`.
- Yo:
  - Escribí mi propia lista de contraseñas de prueba, ajusté el código en base a las sugerencias de la IA, incluido el caso con carácter especial
    (`0812KSEbas!`). Al revisarla, ajusté los valores límite para que quedaran justo en
    los bordes (7, 8, 20 y 21) y agregué los casos que faltaban (sin número, vacío y `None`).
  - Elegí organizar las pruebas por técnica (válidas, valores límite y negativas), para que
    el nombre de cada prueba indique qué verifica.
  - Ejecuté las pruebas y verifiqué que todas pasan.

### Parte 3 - Script de UI mobile
- IA: generó la mayor parte del código, ya que no tenía mucha experiencia en la parte de UI mobile, ya que no he llevado aún el curso de diseño de aplicaciones móviles (4to año), además, la IA me
  explicó Page Object, locators, esperas explícitas, fixtures y capabilities, que eran
  conceptos nuevos para mí.
- Yo: revisé el código parte por parte. Pregunté acerca del código y como este se comportaba para entender el flujo. Verifiqué la estructura
  con `pytest --collect-only` y `pytest --fixtures`.

### Parte 4 - Reporte de bug 
- IA: Entender la diferencia entre prioridad y severidad, y sugerencia de preguntas abiertas a incógnitas que no me quedaban del todo claras. 
- Yo: Realicé el reporte, entendiendo las diferencias entre severidad y la prioridad, además consideré algunas preguntas abiertas para incluirlas en el reporte del bug. 