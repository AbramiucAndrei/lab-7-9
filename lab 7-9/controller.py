from domain import Student,Disciplina,Validate_student,Validate_disciplina,ValidationError
#from UI import *
def get_maxID(lista):
    """
    :return: id ul maxim ce a fost gasit in lista de studenti sau discipline
    """
    maxID = 0
    for elem in lista:
        if elem.get_id() > maxID:
            maxID = elem.get_id()

    return maxID

def creeaza_student(nume,lista_stud):
    """
    se primeste numele studentului ca parametru, student ce trebuie introdus in lista_stud
    se returneaza studentul nou
    """
    studID=get_maxID(lista_stud)+1
    student_nou= Student(studID,nume)
    return student_nou

def creeaza_disciplina(nume,profesor,lista_disc):
    """
    se creeaza si returneaza o noua disciplina cu numele si profesorul primiti prin parametru
    iar id ul generat automat
    """
    discID=get_maxID(lista_disc)+1
    disciplina_noua= Disciplina(discID,profesor,nume)
    return disciplina_noua

