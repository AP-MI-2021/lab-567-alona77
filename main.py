from tests.test_crud import test_create, test_read, test_update, test_delete
from tests.test_operatii import test_pret_modificat, test_trecere_superior, test_pret_max
from UserInterface.console import run_ui

def main():
    run_ui()
    
if __name__ == '__main__':
    test_create()
    test_read()
    test_update()
    test_delete()
    test_pret_modificat()
    test_trecere_superior()
    #test_ordonare_descresc_dupa_pret()
    test_pret_max()
    main()