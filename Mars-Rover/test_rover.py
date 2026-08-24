from main_rover import informar_posicion_orientacion

def test_informar_posicion_orientacion():
    assert informar_posicion_orientacion(1,2,"N") == "1,2,N"
def test_girar():
    assert girar("L") == "O" and girar("R") == "N"
