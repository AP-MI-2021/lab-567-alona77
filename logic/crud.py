from domain.rezervare import creeaza_rezervare, get_id

def create(lst_rezervari, id_rezervare, nume, clasa, pret, checkin_facut, undo_lst: list, redo_lst: list):
    """
    Crearea unei noi rezervari
    :param lst_rezervare: lista de rezervari
    :param id_rezervare: id-ul unic al rezervarii
    :param nume: numele persoanei pe care s-a facut rezervarea
    :param clasa: tipul clasei (economy, economy plus, business)
    :param pret: pretul rezervarii
    :param checkin_facut: daca s-a facut chechin-ul sau nu (da sau nu)
    :param undo_lst:lista inainte de vreo modificare
    :param redo_lst:
    :return: lista noua obt prin concatenarea vechii liste (lst_rezervari) si a noii rezervari
    """
    if read(lst_rezervari, id_rezervare) is not None:
        raise ValueError ("Exista deja rezervare cu acest id")

    rezervare=creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin_facut)

    undo_lst.append(lst_rezervari)
    redo_lst.clear()

    return lst_rezervari+[rezervare]


def read(lst_rezervari , id_rezervare: int=None):
    """
    Citeste o rezervare dupa id_ul unic
    :param lst_rezervare: lista rezervari
    :param id_rezervare: id-ul unic dupa care se citeste rezervarea
    :return: rezervarea ceruta sau toata lista daca id_rezervare este None sau None daca nu exista rezervare cu id-ul cerut
    """
    if not id_rezervare:
        return lst_rezervari

    rezervare_cu_id = None
    for rezervare in lst_rezervari:
        if get_id(rezervare) == id_rezervare:
            rezervare_cu_id=rezervare

    if rezervare_cu_id:
        return rezervare_cu_id
    return None


def update(lst_rezervari, new_rezervare, undo_lst, redo_lst):
    """
    Actualizeaza/ modifica in lista de rezervari o rezervare 
    :param lst_rezervari: lista de rezervari
    :param new_rezervare: rezervarea care trebuie modificata
    :param undo_lst: lista asupra careia are efect comanda "Undo"
    :param redo_lst: lista asupra careia actioneaza comanda "redo"
    :return: lista noua cu rezervarea modificata
    """
    if read(lst_rezervari, get_id(new_rezervare)) is None:
        raise ValueError ("Nu exista rezervare cu id-ul acesta pentru a fi actualizata")

    new_rezervari=[]
    for rezervare in lst_rezervari:
        if get_id(rezervare) != get_id(new_rezervare):
            new_rezervari.append(rezervare)
        else:
            new_rezervari.append(new_rezervare)

    undo_lst.append(lst_rezervari)
    redo_lst.clear()

    return new_rezervari


def delete(lst_rezervari, id_rezervare, undo_lst, redo_lst):
    """
    Stergerea unei rezervari dupa un id dat
    :param lst_rezervari: lista de rezervari
    :param is_rezervare: id ul rezervarii care trebuie sterse
    :param undo_lst: lista asupra careia are efect comanda "Undo"
    :param redo_lst: lista asupra careia actioneaza comanda "redo"
    :return: lista fara rezervarea cu id-ul dat
    """
    if read(lst_rezervari, id_rezervare) is None:
        raise ValueError ("Nu exista rezervare cu id-ul acesta pentru a fi stearsa")

    new_rezervari=[]
    for rezervari in lst_rezervari:
        if get_id(rezervari)!=id_rezervare:
            new_rezervari.append(rezervari)

    undo_lst.append(lst_rezervari)
    redo_lst.clear()
    return new_rezervari


        
    







