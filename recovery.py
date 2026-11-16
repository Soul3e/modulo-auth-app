def recuperar_contrasena(correo):
    if correo == "usuario@institucion.edu":
        print("Se ha enviado un enlace de recuperacion al correo.")
    else:
        print("El correo no esta registrado.")


# Prueba de recuperacion
recuperar_contrasena("usuario@institucion.edu")
