from logic.operatii import trecere_superior
from domain.rezervare import creeaza_rezervare

def get_data():
    return [creeaza_rezervare(1, 'John', 'economy', 120, True), 
    creeaza_rezervare(2, 'Marie', 'business', 300, False),
    creeaza_rezervare(3, 'Alex', 'economy plus', 200, True)]


def test_trecere_superior():
    lst_rezervari=get_data()
    lst_noua_rezervari=trecere_superior(lst_rezervari)
    assert len(lst_rezervari) == len(lst_noua_rezervari)