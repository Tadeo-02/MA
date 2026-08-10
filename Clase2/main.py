
#En grupos. Desarrollan la funcionalidad que les pido del String Calculator. Usando TDD. Haciendo Push en cada Verde.
#Cuando terminan la funcionalidad, avisan en el canal de chat del grupo y yo les pido mas funcionalidad.
import unittest

def test_suma_dos_numeros():
    assert sumar("1,2") == 3

def test_suma_vacio():
    assert sumar("") == 0

def test_suma_un_numero():
    assert sumar("1") == 1


