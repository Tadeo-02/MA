ORIENTACIONES = ["N", "E", "S", "O"]
DELTAS = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "O": (-1, 0)}

orientacion_actual = "N"
pos_actual = [0, 0]

def informar_posicion_orientacion(x, y, orientacion):
    return f"{x},{y},{orientacion}"

def girar(direccion):
    global orientacion_actual
    idx = ORIENTACIONES.index(orientacion_actual)
    if direccion == "L":
        orientacion_actual = ORIENTACIONES[(idx - 1) % 4]
    elif direccion == "R":
        orientacion_actual = ORIENTACIONES[(idx + 1) % 4]
    return orientacion_actual

def _delta(signo):
    dx, dy = DELTAS[orientacion_actual]
    return dx * signo, dy * signo

def avanzar(direccion):
    return _delta(1)

def retroceder(direccion):
    return _delta(-1)

def moverse(comandos):
    global pos_actual
    for c in comandos:
        if c in ("L", "R"):
            girar(c)
        elif c == "F":
            dx, dy = _delta(1)
            pos_actual[0] += dx
            pos_actual[1] += dy
        elif c == "B":
            dx, dy = _delta(-1)
            pos_actual[0] += dx
            pos_actual[1] += dy
    return tuple(pos_actual) + (orientacion_actual,)

def cadena_comandos(comandos):
    global pos_actual, orientacion_actual
    pos_actual = [0, 0]
    orientacion_actual = "N"
    return moverse(comandos)