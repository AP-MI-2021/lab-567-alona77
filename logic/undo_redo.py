from typing import List


def do_undo(undo_lst: list, redo_lst: list, curent_lst:list):
    """
    Se construieste fct de undo (anularea ultimei comenzi asupra listei)
    :param undo_lst:
    :param redo_lst:
    :param curent_lst: 
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
    :param undo_lst:
    :param redo_lst:
    :param current_lst:
    :return:
    """
    if redo_lst:
        top_redo=redo_lst.pop()
        undo_lst.append(current_lst)
        return top_redo

    return None

