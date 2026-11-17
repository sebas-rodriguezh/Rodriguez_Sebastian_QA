import pytest
from shopgo.validaciones import calcular_envio, validar_password

# --- Validar Password. 

@pytest.mark.parametrize(
        "password",
        ["Sebastian123", "0812KSEbas!"],
        ids=["cumple_todas_reglas", "contiene_especial"],
        )
def test_password_valida_es_aceptada(password):
    assert validar_password(password) is True

@pytest.mark.parametrize(
    "password, esperado",
    [
        ("Sebas08", False), #7
        ("Sebas081", True), #8
        ("Sebas0812abcdefghijk", True), #20
        ("Sebas0812abcdefghijkl", False), #21
    ],
    ids=["7_chars", "8_chars", "20_chars", "21_chars"],
    )
def test_password_valores_limite_de_longitud(password, esperado):
    assert validar_password(password) is esperado

@pytest.mark.parametrize(
    "password",
    ["sebas0812","soloSebas", 3423, "Soy Sebas1", " Sebas342", "", None],
    ids=["sin_mayuscula", "sin_numero", "no_string", "con_espacios", "espacio_inicio", "vacio", "none"],
    )
def test_password_invalida_es_rechazada(password):
    assert validar_password(password) is False

# --- Calcular envio 

@pytest.mark.parametrize(
     "subtotal, envio_esperado",
     [
         (0, 2500),
         (24999, 2500),
         (24999.99, 2500),
         (25000, 0),
         (25000.01, 0),
         (100000, 0),
     ],
     ids=["subtotal_0", "subtotal_24999", "subtotal_24999.99", "subtotal_25000", "subtotal_25000.01", "subtotal_100000"],
     )
def test_calcular_envio_segun_subtotal(subtotal, envio_esperado):
    assert calcular_envio(subtotal) == envio_esperado

@pytest.mark.parametrize(
    "subtotal",
    [-1, -0.01],
    ids=["menos_uno", "menos_un_centimo"],
)
def test_calcular_envio_con_subtotal_negativo_lanza_value_error(subtotal):
    with pytest.raises(ValueError):
        calcular_envio(subtotal)
