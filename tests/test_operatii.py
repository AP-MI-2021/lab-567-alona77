from logic.operatii import det_max_fiecare_clasa, ordonare_descresc_dupa_pret, pret_modificat, trecere_superior, suma_pret_nume
from domain.rezervare import creeaza_rezervare, get_checkin_facut, get_clasa, get_nume, get_pret
from logic.undo_redo import do_redo, do_undo

def get_data():
    return [creeaza_rezervare(1, 'John', 'economy', 120, True), 
    creeaza_rezervare(2, 'Marie', 'business', 300, False),
    creeaza_rezervare(3, 'Alex', 'economy plus', 200, True),]

def get_data2():
    return [creeaza_rezervare(1, 'John', 'economy', 120, True), 
    creeaza_rezervare(2, 'Marie', 'business', 300, False),
    creeaza_rezervare(3, 'Alex', 'economy plus', 200, True),
    creeaza_rezervare(4, 'John', 'business', 100, True)]

def test_trecere_superior():
    lst_rezervari=get_data()
    undo_lst=[]
    redo_lst=[]
    lst_noua_rezervari=trecere_superior(lst_rezervari, "John", undo_lst, redo_lst)
    assert len(lst_rezervari) == len(lst_noua_rezervari)
    for rezervare in lst_noua_rezervari:
        if get_nume(rezervare) == "John":
            rezervare_doi=rezervare
    assert get_clasa(rezervare_doi) == "economy plus"
    lst_noua_rezervari=trecere_superior(lst_rezervari, "Marie", undo_lst, redo_lst)
    for rezervare in lst_noua_rezervari:
        if get_nume(rezervare) == "Marie":
            rezervare_trei=rezervare
    assert get_clasa(rezervare_trei) == "business"


def test_pret_modificat():
    lst_rezervari=get_data()
    undo_lst=[]
    redo_lst=[]
    lst_noua_rezervari=pret_modificat(lst_rezervari,50,undo_lst, redo_lst)
    assert len(lst_rezervari)==len(lst_noua_rezervari)
    for rezervare in lst_noua_rezervari:
        if get_nume(rezervare)=="Alex":
            rezervare_noua=rezervare
        elif get_nume(rezervare) == "Marie":
            rezervare_trei=rezervare
    assert get_pret(rezervare_noua) == 100.0
    assert get_pret(rezervare_trei) == 300.00


def test_pret_max():
    lst_rezervari=get_data()
    rezultat=det_max_fiecare_clasa(lst_rezervari)
    assert rezultat == {'economy':120, 'economy plus':200, 'business':300}

def test_ordonare_descresc_dupa_pret():
    lst_rezervari=get_data()
    lst_noua=ordonare_descresc_dupa_pret(lst_rezervari)
        
    assert get_pret(lst_noua[0]) == 300
    assert get_pret(lst_noua[1]) == 200
    assert get_pret(lst_noua[2]) == 120


def test_suma_pret_nume():
    lst_rezervari=get_data2()
    rezultat=suma_pret_nume(lst_rezervari)
    assert rezultat == {'John':220, 'Marie':300, 'Alex':200}


def test_undo_redo_trecere_superior():
    lst_rezervari=get_data()
    undo_lst=[]
    redo_lst=[]
    lst_rezervari=trecere_superior(lst_rezervari, "John", undo_lst, redo_lst)

    for rezervare in lst_rezervari:
        if get_nume(rezervare) == "John":
            rezervare_doi=rezervare
    assert get_clasa(rezervare_doi) == "economy plus"

    lst_rezervari=do_undo(undo_lst, redo_lst, lst_rezervari)
    for rezervare in lst_rezervari:
        if get_nume(rezervare) == "John":
            rezervare_trei=rezervare
    clasa=get_clasa(rezervare_trei)
    assert clasa== "economy"

    lst_rezervari=do_redo(undo_lst, redo_lst, lst_rezervari)
    for rezervare in lst_rezervari:
        if get_nume(rezervare) == "John":
            rezervare_patru=rezervare
    clasa_doi=get_clasa(rezervare_patru)
    assert clasa_doi == "economy plus"


def test_undo_redo_pret_modificat():
    lst_rezervari=get_data()
    undo_lst=[]
    redo_lst=[]

    lst_rezervari=pret_modificat(lst_rezervari,50,undo_lst, redo_lst)
    for rezervare in lst_rezervari:
        if get_nume(rezervare)=="Alex":
            rezervare_noua=rezervare
        elif get_nume(rezervare) == "Marie":
            rezervare_trei=rezervare

    assert get_pret(rezervare_noua) == 100.0
    assert get_pret(rezervare_trei) == 300.00

    lst_rezervari=do_undo(undo_lst, redo_lst, lst_rezervari)
    for rezervare in lst_rezervari:
        if get_nume(rezervare)=="Alex":
            rezervare_patru=rezervare
    assert get_pret(rezervare_patru) == 200.0

    lst_rezervari=do_redo(undo_lst, redo_lst, lst_rezervari)
    for rezervare in lst_rezervari:
        if get_nume(rezervare)=="Alex":
            rezervare_cinci=rezervare
    assert get_pret(rezervare_cinci) == 100.0


     



   