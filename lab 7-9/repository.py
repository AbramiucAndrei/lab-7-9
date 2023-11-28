from domain import Student,Disciplina
def adauga_student(lista,student_nou):
    """

    :param lista: lista de studenti
    :param student_nou: studentul de adaugat
    :return: lista dupa adaugare
    """
    lista.append(student_nou)
    return lista

def adauga_disc(lista,disc_noua):
    """

    :param lista: lista de discipline
    :param disc_noua: disciplina de adaugat
    :return: lista dupa adaugare
    """
    lista.append(disc_noua)
    return lista

def sterge_student(lista,_id):
    """
    stergerea studentului cu id ul primit prin parametru
    :return: lista dupa stergere
    """
    for stud in lista:
        if(stud.get_id()==_id):
            lista.remove(stud)
            return lista

def sterge_disciplina(lista,id):
    """
    stergerea disciplinei cu id ul primit prin parametru\
    :return: lista dupa stergere
    """
    for disc in lista:
        if disc.get_id()==id:
            lista.remove(disc)
            return lista

def modifica_nume(lista,id,nume):
    """
    modificarea numelui studentului/disciplinei cu id ul primit ca parametru
    :param nume: noul nume
    :return: lista dupa modificare
    """
    for elem in lista:
        if elem.get_id()==id:
            elem.set_nume(nume)
            return lista
def modifica_profesor(lista,id,profesor_nou):
    """
    modificarea profesorului de la disciplina cu id ul primit
    :param profesor_nou: numele noului profesor
    :return: lista dupa modificare
    """
    for elem in lista:
        if elem.get_id()==id:
            elem.set_profesor(profesor_nou)
            return lista
