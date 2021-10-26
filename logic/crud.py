from domain.rezervare import creeaza_rezervare, get_id, get_clasa, get_nume, get_checkin_facut, get_pret

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
    rezervare= creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin_facut)
    #lst_rezervari.append(rezervare)
    return lst_rezervari+[rezervare]


def read(lst_rezervari , id_rezervare=None):
    """
    Citeste o rezervare dupa id_ul unic
    :param lst_rezervare: lista rezervari
    :param id_rezervare: id-ul unic dupa care se citeste rezervarea
    :return: rezervarea ceruta || toata lista daca id_rezervare este None
    """
    rezervare_cu_id = None
    for rezervare in lst_rezervari:
        if get_id(rezervare) == id_rezervare:
            rezervare_cu_id=rezervare

    if rezervare_cu_id:
        return rezervare_cu_id
    return lst_rezervari


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


def trecere_superior(lst_rezervari):
    """
    Trecerea tuturor claselor la nivel superior de la un nume citit la o clasa superioara
    :param lst_rezervare: lista de rezervari
    :return: lista noua cu clasele upgradated
    """
    nume=input("Dati numele pt care rezervarea se upgradeaza: ")
    new_list=[]
    exista=0
    for rezervare in lst_rezervari:
        if get_nume(rezervare) == nume :
            exista=1
            if get_clasa(rezervare) == 'economy':
                    id=get_id(rezervare)
                    pret=get_pret(rezervare)
                    val=get_checkin_facut(rezervare)
                    val_rezv=creeaza_rezervare(id,nume,'economy plus',pret,val)
                    new_list.append(val_rezv)
            elif get_clasa(rezervare) == 'economy plus':
                    id=get_id(rezervare)
                    pret=get_pret(rezervare)
                    val=get_checkin_facut(rezervare)
                    val_rezv=creeaza_rezervare(id,nume,'business',pret,val)
                    new_list.append(val_rezv)
            elif get_clasa(rezervare) == 'business':
                new_list.append(rezervare)
        else:
            new_list.append(rezervare)

    if exista == 0 :
        print("nu este numele in lista \n")
    else:
        return new_list

    
def pret_modificat(lst_rezervari):
    """
    Modifica pretul in cazul rezervarilor care au checkin True
    :param lst_rezervari: lista rezervare
    :return: lsita noua cu preturile modificate
    """
    gasit=0
    new_list=[]
    procent=int(input("Introdu procent: "))
    for rezervare in lst_rezervari:
        if get_checkin_facut(rezervare) :
            gasit=1
            pret=get_pret(rezervare)-(procent*get_pret(rezervare))/100
            id=get_id(rezervare)
            clasa=get_clasa(rezervare)
            nume=get_nume(rezervare)
            val=creeaza_rezervare(id,nume,clasa,pret,True)
            new_list.append(val)
        else:
            new_list.append(rezervare)
    if gasit == 0:
        print("Nu exista rezervari care au facut checkin-ul\n")
    else:
        return new_list

        
    







