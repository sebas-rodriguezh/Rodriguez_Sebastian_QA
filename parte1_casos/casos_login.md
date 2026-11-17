# Casos de prueba | Inicio de sesión ShopGo

Datos de prueba: usuario registrado sebas@shopgo.com / Sebas0812

| ID | Título | Precondiciones | Pasos | Resultado esperado | Prioridad |
|---|---|---|---|---|---|
| TC-01 | Inicio de sesión con credenciales válidas | Usuario registrado, app instalada | 1. Abrir la app<br>2. Ingresar sebas@shopgo.com y Sebas0000<br>3. Tocar "Iniciar sesión" | Se abre la pantalla principal con el título "Bienvenido" | Alta |
| TC-02 | Contraseña incorrecta | Usuario registrado, app instalada | 1. Abrir la app<br>2. Ingresar sebas@shopgo.com y Sebas0000<br>3. Tocar "Iniciar sesión" | Aparece "Correo o contraseña incorrectos" y no se inicia sesión | Alta |
| TC-03 | Usuario no registrado | El correo noexiste@shopgo.com no está registrado | 1. Abrir la app<br>2. Ingresar noexiste@shopgo.com y Sebas0812<br>3. Tocar "Iniciar sesión" | Aparece "Correo o contraseña incorrectos" (Para no revelar si el correo existe) | Alta |
| TC-04 | Correo con formato inválido | App instalada | 1. Abrir la app<br>2. Ingresar sebas.shopgo.com (sin @) y Sebas0812<br>3. Tocar "Iniciar sesión" | No se inicia sesión y se muestra un mensaje de error | Media |
| TC-05 | Campos vacíos | App instalada | 1. Abrir la app<br>2. Dejar correo y contraseña vacíos<br>3. Tocar "Iniciar sesión" | No se inicia sesión, se muestra un mensaje de error y la app no se cierra | Media |
| TC-06 | Contraseñas fuera de los límites (7 y 21 caracteres) | App instalada | 1. Abrir la app<br>2. Ingresar correo válido y Sebas08 (7)<br>3. Tocar "Iniciar sesión"<br>4. Repetir con Sebas0812abcdefghijkl (21) | En ambos intentos no se inicia sesión y se muestra un mensaje de error | Alta |
| TC-07 | Contraseñas en los límites válidos (8-20 caracteres) | Usuarios registrados con Sebas081 (8) y Sebas0812abcdefghijk (20) | 1. Iniciar sesión con la contraseña de 8 caracteres<br>2. Cerrar sesión<br>3. Iniciar sesión con la de 20 caracteres | En ambos casos se abre "Bienvenido" | Alta |
| TC-08 | Correo sin nombre antes del @ | App instalada | 1. Abrir la app<br>2. Ingresar @shopgo.com y Sebas0812<br>3. Tocar "Iniciar sesión" | No se inicia sesión y se muestra un mensaje de error | Media |
| TC-09 | Contraseña sin mayúscula, sin número o con espacio | Una cuenta distinta para cada variante, para no activar el bloqueo | 1. Abrir la app<br>2. Probar por separado: sebas0812, Sebasabcd, Sebas 0812<br>3. Tocar "Iniciar sesión" en cada intento | En los tres intentos no se inicia sesión y se muestra un mensaje de error | Media |
| TC-10 | Bloqueo tras 3 intentos fallidos seguidos | Usuario registrado sin intentos fallidos previos | 1. Ingresar contraseña incorrecta 3 veces seguidas<br>2. Ingresar la contraseña correcta<br>3. Esperar 5 minutos y repetir el paso 2 | Paso 2: no permite entrar (cuenta bloqueada). Paso 3: se abre "Bienvenido" | Alta |
| TC-11 | Inicio de sesión sin conexión | Usuario registrado, modo avión activado | 1. Abrir la app<br>2. Ingresar credenciales válidas<br>3. Tocar "Iniciar sesión" | Se informa que no hay conexión; la app no se cierra ni queda cargando para siempre | Alta |
| TC-12 | Rotar la pantalla con datos ingresados | App instalada | 1. Abrir la app en vertical<br>2. Ingresar correo y contraseña<br>3. Rotar a horizontal y volver a vertical | Los datos se conservan y la pantalla se adapta sin errores | Media |