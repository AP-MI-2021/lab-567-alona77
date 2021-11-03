from os import lseek
from logic.file_logic import read_lista, save_lista
from logic.operatii import ordonare_descresc_dupa_pret
from UserInterface.console import handle_delete

def read_list():
    lst = []
    lst_str = input ("Introduceti comenzile respectand instructiunea: ")
    lst_str_split = lst_str.split(';')
    for com_str in lst_str_split:
        lst.append(com_str)
    return lst

def alt_main():
    filename = ' text.txt' 
    try:
        lst_rezervari=read_lista(filename)
    except Exception:
        print('Nu s-a putut citi fisireul')
        lst_rezervari=[]
    
    while True:
        print("Intr-o linie de comanda scrie comenzile care doresti indeplinite, separate prin ';'la final scriind comanda exit")
        print("1.Pt afisarea tuturor vei scrie in linia de comanda : showall")
        print("2.Pt ordonarea lor descresc vei scrie in linia de comanda : ordonare ")
        print("3.Pt a sterge o rezervare vei scrie linia de comanda : delete,id ")
        print("4.Pt iesirea din meniu introduceti: exit")

        

        lista_comenzi=read_list()

        if "showall" in lista_comenzi:
            print(lst_rezervari)
        for index in lista_comenzi:
            if "delete" in index:
                id_din_lista=index.split(',')[1]
                handle_delete(lst_rezervari, int(id_din_lista))
                save_lista(filename, lst_rezervari)
                print("stergere realizata cu succes")
        if "ordonare" in lista_comenzi:
            lst_noua=ordonare_descresc_dupa_pret(lst_rezervari)
            print(f'Lista ordonata descresc este: \n {lst_noua}')
        if "exit" in lista_comenzi:
            break
            


