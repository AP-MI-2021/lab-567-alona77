from typing import List


def do_undo(undo_lst: list, redo_lst: list, curent_lst:list):
    """
    Se construieste fct de undo (anularea ultimei comenzi asupra listei)
    :param undo_lst: lista de dinainte de vreo modificare
    :param redo_lst:lista asupra careia a avut loc modificare
    :param curent_lst: lista de rezervari in cazul acestei pb
    :return: lista asupra careia a actionat undo
    """
    if undo_lst:
        top_undo=undo_lst.pop()
        redo_lst.append(curent_lst)
        return top_undo
    
    return None


def do_redo(undo_lst: list, redo_lst : list, current_lst: list):
    """
    fct de redo (care se poate aplica doar asupra unui undo)
    :param undo_lst: lista care retine lista inainte de modificare
    :param redo_lst:lista care a suferit modificare
    :param current_lst:lista de rezervari
    :return:lista asupra careia a actionat comanda redo
    """
    if redo_lst:
        top_redo=redo_lst.pop()
        undo_lst.append(current_lst)
        return top_redo

    return None

