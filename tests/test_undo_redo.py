from domain.rezervare import get_id
from logic.crud import create
from logic.undo_redo import do_redo, do_undo

def test_redo_undo():
    lst_rezervari=[]
    undo_lst=[]
    redo_lst=[]
            
    lst_rezervari=create(lst_rezervari, 1, 'Karina', 'economy', 200, True, undo_lst, redo_lst)
    lst_rezervari=create(lst_rezervari, 2, 'John', 'economy plus', 190, False, undo_lst, redo_lst)
    lst_rezervari=create(lst_rezervari, 3, 'Alex', 'business', 380, True, undo_lst, redo_lst)

    lst_rezervari=do_undo(undo_lst, redo_lst, lst_rezervari)
    gasit = 0
    for rezervare in lst_rezervari:
        if get_id(rezervare)==1:
            gasit=gasit+1
        elif get_id(rezervare) == 2:
            gasit=gasit+1
    assert gasit == 2
   # assert lst_rezervari == [(1, 'Karina', 'economy', 200, True), (2, 'John', 'economy plus', 190, False)] 
   
    lst_rezervari=do_undo(undo_lst, redo_lst, lst_rezervari)
    gasit = 0 
    for rezervare in lst_rezervari:
        if get_id(rezervare)==1:
            gasit = 1
    assert gasit == 1
    #assert lst_rezervari== [(1, 'Karina', 'economy', 200, True)]

    lst_rezervari=do_undo(undo_lst, redo_lst, lst_rezervari)
    assert lst_rezervari == []
    lst_patru=do_undo(undo_lst, redo_lst, lst_rezervari)
    assert lst_patru == None
        
    lst_rezervari=create(lst_rezervari, 4, 'Maria', 'economy', 200, True, undo_lst, redo_lst)
    lst_rezervari=create(lst_rezervari, 5, 'Stephan', 'economy plus', 190, False, undo_lst, redo_lst)
    lst_rezervari=create(lst_rezervari, 6, 'Amy', 'business', 380, True, undo_lst, redo_lst)

    lst_redo=do_redo(undo_lst, redo_lst, lst_rezervari)
    assert lst_redo == None

    lst_rezervari=do_undo(undo_lst, redo_lst, lst_rezervari)
    lst_rezervari=do_undo(undo_lst, redo_lst, lst_rezervari)
    gasit = 0
    for rezervare in lst_rezervari:
        if get_id(rezervare) == 4:
            gasit = 1
    assert gasit == 1
    #assert lst_rezervari == [(4, 'Maria', 'economy', 200, True)]

    lst_rezervari=do_redo(undo_lst, redo_lst, lst_rezervari)
    gasit=0
    for rezervare in lst_rezervari:
        if get_id(rezervare) == 4:
            gasit=gasit+1
        elif get_id(rezervare) == 5:
            gasit=gasit+1
    assert gasit == 2
    #assert lst_rezervari == [(4, 'Maria', 'economy', 200, True),(5, 'Stephan', 'economy plus', 190, False)]
    
    lst_rezervari=do_redo(undo_lst, redo_lst, lst_rezervari)
    gasit=0
    for rezervare in lst_rezervari:
        if get_id(rezervare) == 4:
            gasit=gasit+1
        elif get_id(rezervare) == 5:
            gasit=gasit+1
        elif get_id(rezervare) == 6:
            gasit=gasit+1
    assert gasit == 3
    #assert lst_rezervari == [(4, 'Maria', 'economy', 200, True),(5, 'Stephan', 'economy plus', 190, False),(6, 'Amy', 'business', 380, True)]

    lst_rezervari=do_undo(undo_lst, redo_lst, lst_rezervari)
    lst_rezervari=do_undo(undo_lst, redo_lst, lst_rezervari)
    gasit=0
    for rezervare in lst_rezervari:
        if get_id(rezervare) == 4:
            gasit=gasit+1
    assert gasit == 1
    #assert lst_rezervari == [(4, 'Maria', 'economy', 200, True)] 

    lst_rezervari=create(lst_rezervari, 7, 'Ana', 'business', 100, True, undo_lst, redo_lst)
    lst_redo_doi=do_redo(undo_lst, redo_lst, lst_rezervari)
    assert lst_redo_doi == None
    gasit=0 
    for rezervare in lst_rezervari:
        if get_id(rezervare) == 4:
            gasit=gasit+1
        elif get_id(rezervare) == 7:
            gasit=gasit+1
    assert gasit == 2
    #assert lst_rezervari == [(4, 'Maria', 'economy', 200, True), (7, 'Ana', 'business', 100, True)]

    lst_rezervari=do_undo(undo_lst, redo_lst, lst_rezervari)
    gasit=0
    for rezervare in lst_rezervari:
        if get_id(rezervare) == 4:
            gasit=gasit+1
    assert gasit == 1
    #assert lst_rezervari == [(4, 'Maria', 'economy', 200, True)]

    lst_rezervari=do_undo(undo_lst, redo_lst, lst_rezervari)
    assert lst_rezervari == []

    lst_rezervari=do_redo(undo_lst, redo_lst, lst_rezervari)
    lst_rezervari=do_redo(undo_lst, redo_lst, lst_rezervari)
    gasit=0 
    for rezervare in lst_rezervari:
        if get_id(rezervare) == 4:
            gasit=gasit+1
        elif get_id(rezervare) == 7:
            gasit=gasit+1
    assert gasit == 2
    #assert lst_rezervari == [(4, 'Maria', 'economy', 200, True),(7, 'Ana', 'business', 100, True)]

    lst_alt_redo=do_redo(undo_lst, redo_lst, lst_rezervari)
    assert lst_alt_redo==None