from domain.rezervare import get_checkin_facut, get_clasa, get_id, get_nume, get_pret, get_str,creeaza_rezervare

def trecere_superior(lst_rezervari, nume: str):
    """
    Trecerea tuturor claselor la nivel superior de la un nume citit la o clasa superioara
    :param lst_rezervare: lista de rezervari
    :return: lista noua cu clasele upgradated
    """
    if nume.isalpha() is False:
        raise ValueError ("Numele nu este valabil")

    new_list=[]
    exista=0
    for rezervare in lst_rezervari:
        if nume in get_nume(rezervare) :
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
        return ("Numele nu este in lista \n")
    else:
        return new_list

    
def pret_modificat(lst_rezervari, procent):
    """
    Modifica pretul in cazul rezervarilor care au checkin True
    :param lst_rezervari: lista rezervare
    :return: lsita noua cu preturile modificate
    """
    if not (0<= procent <=100):
        raise ValueError ("Procentul trebuie sa fie intre 0 si 100") 

    gasit=0
    new_list=[]
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
        return("Nu exista rezervari care au facut checkin-ul\n")
    else:
        return new_list


def det_max_fiecare_clasa(lst_rezervari):
    """
    Determina pretul maxim pt fiecare clasa: economy, economy plus, business
    :param lst_rezervari: lista de rezervari
    :return: dictionar cu perechile cheia : clasa si valoarea: pretul maxim pt clasa respectiva
    """
    rezultat={}
    for rezervare in lst_rezervari:
        clasa=get_clasa(rezervare)
        pret=get_pret(rezervare)
        if clasa not in rezultat:
            rezultat[clasa]=pret
        elif pret>rezultat[clasa]:
                rezultat[clasa]=pret
    return rezultat

def ordonare_descresc_dupa_pret(lst_rezervari):
    """
    Ordoneaza descrescator rezervarile dupa pret
    :param lst_rezervare: lista de rezervari
    :return: lista noua in care rezervarile sunt ordonate descresc
    """
    lst_noua=sorted(lst_rezervari, key= get_pret, reverse=True)
    return lst_noua

def suma_pret_nume(lst_rezervari):
    """
    Se da pentru fiecare nume suma totala pe care o are de platit pentru rezervarile de pe numele lor
    :param lst_rezervari: lista de rezervari
    :return: dictionar cu perechile cheia:numele persoanei si valorea:costul total al rezervarilor
    """
    rezultat={}
    for rezervare in lst_rezervari:
        pret=get_pret(rezervare)
        nume=get_nume(rezervare)
        if nume not in rezultat:
            rezultat[nume]=pret
        else:
            rezultat[nume]+=pret
    return rezultat