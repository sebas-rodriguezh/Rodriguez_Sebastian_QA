def validar_password(password):
    "True si la contraseña cumple con las reglas ShopGo."

    if not isinstance(password, str):
        return False

    if not (8 <= len(password) <= 20):
        return False

    if not any(c.isupper() for c in password):
        return False

    if not any(c.isdigit() for c in password):
        return False

    if any(c.isspace() for c in password):
        return False
    
    return True


def calcular_envio(subtotal: float) -> int:
    "Devuelve el costo de envío en colones según el subtotal."
    if subtotal < 0:
        raise ValueError("El subtotal NO puede ser negativo")
    if subtotal >= 25000:
        return 0
    return 2500