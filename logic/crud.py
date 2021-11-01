from domain.rezervare import creeaza_rezervare, get_id

def create(lst_rezervari, id_rezervare, nume, clasa, pret, checkin_facut):
    """
    Crearea unei noi rezervari
    :param lst_rezervare: lista de rezervari
    :param id_rezervare: id-ul unic al rezervarii
    :param nume: numele persoanei pe care s-a facut rezervarea
    :param clasa: tipul clasei (economy, economy plus, business)
    :param pret: pretul rezervarii
    :param checkin_facut: daca s-a facut chechin-ul sau nu (da sau nu)
    :return: lista noua obt prin concatenarea vechii liste (lst_rezervari) si a noii rezervari
    """
    if read(lst_rezervari,id_rezervare) is None:
        raise ValueError (f'Exista deja rezervare cu id-ul {id_rezervare}')

    rezervare=creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin_facut)
    #lst_rezervari.append(rezervare)
    return lst_rezervari+[rezervare]


def read(lst_rezervari , id_rezervare=None):
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


def update(lst_rezervari, new_rezervare):
    """
    Actualizeaza/ modifica in lista de rezervari o rezervare 
    :param lst_rezervari: lista de rezervari
    :param new_rezervare: rezervarea care trebuie modificata
    :return: lista noua cu rezervarea modificata
    """
    new_rezervari=[]
    for rezervare in lst_rezervari:
        if get_id(rezervare) != get_id(new_rezervare):
            new_rezervari.append(rezervare)
        else:
            new_rezervari.append(new_rezervare)
    return new_rezervari


def delete(lst_rezervari, id_rezervare):
    """
    Stergerea unei rezervari dupa un id dat
    :param lst_rezervari: lista de rezervari
    :param is_rezervare: id ul rezervarii care trebuie sterse
    :return: lista fara rezervarea cu id-ul dat
    """
    new_rezervari=[]
    for rezervari in lst_rezervari:
        if get_id(rezervari)!=id_rezervare:
            new_rezervari.append(rezervari)
    return new_rezervari


        
    







