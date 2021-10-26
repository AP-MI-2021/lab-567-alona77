import json

def read_lista(filename):
    """
    Citeste fisierul cu lista de dictionare care rep rezervari
    :param filename: numele fisierului
    :return: lista
    """
    with open(filename, 'r') as f:
        return json.load(f)


def save_lista(filename, lst_rezervari):
    """
    Salveaza lista modificata
    :param filename: fisierul in care se face salvarea
    :lst_rezervari:lista care va fi salvata
    """
    with open(filename, 'w') as f:
        json.dump(lst_rezervari, f)

