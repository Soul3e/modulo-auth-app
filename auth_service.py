
def validar_credenciales(usuario, contrasena):
    if usuario == "admin" and contrasena == "1234":
        return True
    else:
        return False


# Prueba de autenticacion
resultado = validar_credenciales("admin", "1234")

if resultado:
    print("Acceso permitido")
else:
    print("Acceso denegado")
