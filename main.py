from tests.test_crud import test_create, test_read, test_update, test_delete
from UserInterface.console import run_ui

def main():
    run_ui()
    
if __name__ == '__main__':
    test_create()
    test_read()
    test_update()
    test_delete()
    main()