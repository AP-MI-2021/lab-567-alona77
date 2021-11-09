from tests.test_crud import test_create, test_read, test_update, test_delete
from tests.test_operatii import test_pret_modificat, test_trecere_superior, test_pret_max, test_ordonare_descresc_dupa_pret, test_suma_pret_nume
from UserInterface.console import run_ui
from UserInterface.comand import alt_main

def main():
    run_ui()
    #alt_main()
    
if __name__ == '__main__':
    test_create()
    test_read()
    test_update()
    test_delete()
    test_pret_modificat()
    test_trecere_superior()
    test_ordonare_descresc_dupa_pret()
    test_pret_max()
    test_suma_pret_nume()
    main()