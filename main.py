from tests.test_crud import test_create, test_read, test_update, test_delete
from UserInterface.console import run_ui
from logic.crud import create
from domain.rezervare import get_id, creeaza_rezervare


def main():
    rezervari=[]
    rezervari=create(rezervari, 1, 'John', 'economy', 120, False)
    rezervari=run_ui(rezervari)
    
if __name__ == '__main__':
    test_create()
    test_read()
    test_update()
    test_delete()
    main()