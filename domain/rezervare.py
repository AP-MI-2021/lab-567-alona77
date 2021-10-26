def creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin_facut):
    """
    Creeaza o rezervare
    :param id_rezervare: id-ul unic al rezervarii
    :param nume: numele persoanei pe care s-a facut rezervarea
    :param clasa: tipul clasei (economy, economy plus, business)
    :param pret: pretul rezervarii
    :param checkin_facut: daca s-a facut chechin-ul sau nu (da sau nu)
    :return: o rezervare
    """
    return {
        'id': id_rezervare, 
        'nume': nume, 
        'clasa': clasa, 
        'pret': pret , 
        'checkin_facut': checkin_facut
    }

def get_id(rezervare):
    """
    Get id-ul rezervarii
    """
    return rezervare['id']


def get_nume(rezervare):
    """
    Get nume_rezervare
    """
    return rezervare['nume']


def get_clasa(rezervare):
    """
    Get nume persoana pe care s-a facut rezervarea
    """
    return rezervare['clasa']


def get_pret(rezervare):
    """
    Get pretul rezervarii
    """
    return rezervare['pret']


def get_checkin_facut(rezervare):
    """
    Daca checkin-ul este facut sau nu
    """
    return rezervare['checkin_facut']


def get_str(rezervare):
    return f'Rezervarea cu id-ul {get_id(rezervare)}, pe numele {get_nume(rezervare)}, \
    cu clasa {get_clasa(rezervare)}, a carui pret este {get_pret(rezervare)}, iar chekin-ul {get_checkin_facut(rezervare)}'

