from domain.rezervare import creeaza_rezervare, get_id
from logic.crud import create, read, update, delete

def get_data():
    return [creeaza_rezervare(1, 'John', 'economy', 120, True), 
    creeaza_rezervare(2, 'Marie', 'business', 300, False),
    creeaza_rezervare(3, 'Alex', 'economy plus', 200, True)]


def test_create():
    lt_rezervari= get_data()
    params = (4, 'Tim', 'economy', 150, False)
    rezv_new = creeaza_rezervare(*params)
    new_rezervari=create(lt_rezervari, *params)
   # assert new_rezervari[-1] == rezv_new 
    assert len(new_rezervari) == len(lt_rezervari) +1

    """
    alta varianta de a verifica
    found=False
    for rezervare in new_rezervari:
        if rezervare == rezv_new:
            found = True
    """    
    assert rezv_new in new_rezervari


def test_read():
    lst_rezervari=get_data()
    some_rezv = lst_rezervari[1]
    assert read(lst_rezervari, get_id(some_rezv)) == some_rezv
    assert read(lst_rezervari, None) == lst_rezervari


def test_update():
    lst_rezervari=get_data()
    rezv_updated=creeaza_rezervare(1,'nou nume', 'economy', 120, True)
    up_rezvervari=update(lst_rezervari,rezv_updated)
    assert rezv_updated in up_rezvervari
    assert rezv_updated not in lst_rezervari
    assert len(up_rezvervari) == len(lst_rezervari)


def test_delete():
    lst_rezervari=get_data()
    id_del=1
    rezv_del=read(lst_rezervari, id_del)
    del_lst=delete(lst_rezervari, id_del)
    assert rezv_del not in del_lst
    assert rezv_del in lst_rezervari
    assert len(del_lst) == len(lst_rezervari)-1


