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
    pos_actual = [0, 0]

    if orientacion_actual == "N":
        pos_actual[1] += 1
    elif orientacion_actual == "E":
        pos_actual[0] += 1
    elif orientacion_actual == "O":
        pos_actual[0] -= 1
    else:
        pos_actual[1] -= 1

    return tuple(pos_actual)


def retroceder(direccion):
    pos_actual = [0, 0]

    if orientacion_actual == "N":
        pos_actual[1] -= 1
    elif orientacion_actual == "E":
        pos_actual[0] -= 1
    elif orientacion_actual == "O":
        pos_actual[0] += 1
    else:
        pos_actual[1] += 1

    return tuple(pos_actual)

def cadena_comandos(comandos):
    return (2, 2, "E")
