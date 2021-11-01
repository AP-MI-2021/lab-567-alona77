from domain.rezervare import get_str, get_clasa, get_nume, get_pret, get_checkin_facut, creeaza_rezervare,get_id
from logic.crud import create, read, update, delete
from logic.file_logic import save_lista, read_lista
from logic.operatii import trecere_superior, pret_modificat


def show_menu():
    print("1.Adaugare/stergere/modificare rezervare dupa un id (CRUD)")
    print("2.Upgradarea rezervarilor dupa un nume citit")
    print("3.Ieftinirea rezervarilor cu checkin-ul facut cu un procent p")
    print("4.Determinarea pretului maxim pt fiecare clasa")
    print("5.Ordonarea descresc rezervarilor dupa pret")
    print("6.Afisarea sumelor preturilor pt fiecare nume")
    print("7.Undo")
    print("8.Iesire meniu \n")


def handle_add(lst_rezervari):
    id_rezervare=int(input("Dati id-ul noii rezervari: "))
    nume=input("Dati noul nume: ")
    clasa=input("Dati clasa noii rezervari: ")
    pret=float(input("Dati pretul noii rezervari: "))
    checkin_facut=bool(input("Dati True daca checkin-ul a fost facut, resp False in caz contrar: \n"))
    return create(lst_rezervari, id_rezervare, nume, clasa, pret, checkin_facut)


def show_details(lst_rezervari):
    id_rezervare=int(input("Introduceti id rezervare pt detalii"))
    rezervare=read(lst_rezervari, id_rezervare)
    print(f'Rezervarea e pe numele {get_nume(rezervare)}')
    print(f'Clasa rezervarii este {get_clasa(rezervare)}')
    print(f'Pretul rezervarii este {get_pret(rezervare)}')
    print(f'Checkin-ul este {get_checkin_facut(rezervare)}\n')


def handle_modify(lst_rezervari):
    id_rezervare=int(input("Dati id-ul rezervari care se modifica: "))
    nume=input("Dati noul nume al rezervarii: ")
    clasa=input("Dati noua clasa a rezervari: ")
    pret=float(input("Dati noul pretul al rezervari: "))
    checkin_facut=bool(input("Dati True daca checkin-ul a fost facut, resp False in caz contrar: \n"))
    return update(lst_rezervari, creeaza_rezervare(id_rezervare,nume,clasa,pret, checkin_facut))


def handle_delete(lst_rezervari):
    id_rezervare=int(input("Dati id-ul rezervarii care trebuie stearsa"))
    lst_del=delete(lst_rezervari, id_rezervare)
    return lst_del


def handle_crud(lst_rezervari):
    while True:
        print("1.Adaugare rezervare dupa id")
        print("2.Stergere rezervare dupa id")
        print("3.Modificare rezervare dupa id")
        print("4.Afisare toate rezervari")
        print("5.Revenire meniu principal")
        print("6.Detalii o rezervare \n")


        opt=int(input("Alegeti optiunea: "))
        if opt == 1:
            lst_rezervari=handle_add(lst_rezervari) 
        elif opt == 2:
            lst_rezervari=handle_delete(lst_rezervari)
        elif opt == 3:
            lst_rezervari=handle_modify(lst_rezervari)
        elif opt == 4:
            for rezervare in lst_rezervari:
                print(get_str(rezervare))
        elif opt == 5:
            break
        elif opt == 6:
            show_details(lst_rezervari)
        else:
            print("Optiune invalida")
        return lst_rezervari


def run_ui():
    filename = ' text.txt' 
    try:
        lst_rezervari=read_lista(filename)
    except Exception:
        print('Nu s-a putut citi fisireul')
        lst_rezervari=[]
    while True:
        show_menu()
        opt= int(input("Introduceti optiunea: "))
        if opt == 1:
           lst_rezervari= handle_crud(lst_rezervari)
           save_lista(filename, lst_rezervari)
        elif opt == 2:
            nume=input("Dati numele pt care rezervarea se upgradeaza: ")
            lst_rezervari=trecere_superior(lst_rezervari,nume)
            save_lista(filename,lst_rezervari)
        elif opt == 3:
            procent=int(input("Introdu procent: "))
            lst_rezervari=pret_modificat(lst_rezervari)
            save_lista(filename,lst_rezervari, procent)
        elif opt == 4:
            pass
        elif opt == 5:
            pass
        elif opt == 6:
            pass
        elif opt == 7 :
            pass
        elif opt == 8:
            break

        else:
            print("optiune invalida")
