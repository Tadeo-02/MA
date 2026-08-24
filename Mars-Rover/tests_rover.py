 from main_rover import informar_posicion_orientacion
import pytest

def test_informar_posicion_orientacion():
    assert informar_posicion_orientacion(1,2,"N") == "1,2,N"
    
# git commit -m "RED: rover informa su posicion y orientacion iniciales"   