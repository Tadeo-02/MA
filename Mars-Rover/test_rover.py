from main_rover import informar_posicion_orientacion, girar, avanzar, retroceder

def test_informar_posicion_orientacion():
    assert informar_posicion_orientacion(1,2,"N") == "1,2,N"
def test_girar():
    assert girar("L") == "O" and girar("R") == "N"
def test_avanzar():
    assert avanzar("F") == (0,1)
def test_retroceder():
    assert retroceder("R") == (0,-1)