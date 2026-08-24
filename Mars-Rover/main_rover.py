def informar_posicion_orientacion(x, y, orientacion):
    return f"{x},{y},{orientacion}"

orientacion_actual = "N"
def girar(direccion):
    global orientacion_actual
    orientaciones = ["N", "E", "S", "O"]
    direccion_actual = orientaciones.index(orientacion_actual)
    if (direccion == "L"):
        orientacion_actual = orientaciones[(direccion_actual - 1) % 4]
    elif (direccion == "R"):
        orientacion_actual = orientaciones[(direccion_actual + 1) % 4]
    return orientacion_actual

def avanzar(direccion):
    return (0,1)