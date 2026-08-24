def informar_posicion_orientacion(x, y, orientacion):
    return f"{x},{y},{orientacion}"
def girar(direccion):
    if (direccion == "L"):
        return "O"
    elif (direccion == "R"):
        return "N"