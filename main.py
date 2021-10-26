from tests.test_crud import test_create, test_read, test_update, test_delete
from UserInterface.console import run_ui
from logic.crud import create
from domain.rezervare import get_id, creeaza_rezervare


def main():
    """
    rezervari=[]
    rezervari=run_ui(rezervari)
    """
    run_ui()
    
if __name__ == '__main__':
    test_create()
    test_read()
    test_update()
    test_delete()
    main()