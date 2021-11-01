from logic.operatii import pret_modificat, trecere_superior
from domain.rezervare import creeaza_rezervare, get_clasa,get_pret

def get_data():
    return [creeaza_rezervare(1, 'John', 'economy', 120, True), 
    creeaza_rezervare(2, 'Marie', 'business', 300, False),
    creeaza_rezervare(3, 'Alex', 'economy plus', 200, True)]


def test_trecere_superior():
    lst_rezervari=get_data()
    lst_noua_rezervari=trecere_superior(lst_rezervari, "John")
    assert len(lst_rezervari) == len(lst_noua_rezervari)
    assert get_clasa((1, 'John', 'economy', 120, True)) == "economy plus"
    lst_noua_rezervari=trecere_superior(lst_rezervari, "Marie")
    assert get_clasa((2, 'Marie', 'business', 300, False)) == "business"


def test_pret_modificat():
    lst_rezervari=get_data()
    lst_noua_rezervari=pret_modificat(lst_rezervari,50)
    assert len(lst_rezervari)==len(lst_noua_rezervari)
    assert get_pret((1, 'John', 'economy', 120, True)) == 60.0
    assert get_pret((2, 'Marie', 'business', 300, False)) == 300.00
