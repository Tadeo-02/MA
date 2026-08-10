
#En grupos. Desarrollan la funcionalidad que les pido del String Calculator. Usando TDD. Haciendo Push en cada Verde.
#Cuando terminan la funcionalidad, avisan en el canal de chat del grupo y yo les pido mas funcionalidad.
def sumar(numeros):
    return sum(map(int, numeros.split(",")))


def test_sumar_dos_numeros():
    assert sumar("1,2") == 3

def test_sumar_vacio():
    assert sumar("") == 0

def test_sumar_un_numero():
    assert sumar("1") == 1


