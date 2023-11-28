from domain import Student,Disciplina
from controller import creeaza_student,creeaza_disciplina
from repository import adauga_disc,adauga_student,sterge_student,sterge_disciplina,modifica_nume,modifica_profesor

def citeste_nume(msg):
    """
    functia citeste si returneaza un nume valid
    :param msg: mesajul ce se afiseaza inainte de citirea de la tastatura
    :return: numele,daca este valid
    """
    nume = input(msg).strip()
    for litera in range(0, len(nume)):
        if not (nume[litera].isalpha() or nume[litera] == ' '):
            raise ValueError("Nume invalid")

    return nume


def citeste_student(lista_stud):
    """
    functia citeste numele unui nou student
    :param lista_stud: lista cu studentii de pana acum,in care va fi pus si cel nou
    :return: noul student
    """
    _nume = ""
    try:
        _nume = citeste_nume("Introduceti numele studentului: ")
        return creeaza_student(_nume, lista_stud)
    except ValueError as er:
        print(er)
        return citeste_student(lista_stud)


def citeste_disc(lista_disc):
    """
    functia citeste o noua disciplina
    :param lista_disc: lista cu disciplinele
    :return: noua disciplina citita
    """
    try:
        nume_disc = citeste_nume("Introduceti numele disciplinei: ")
        profesor_disc = citeste_nume("Introduceti numele profesorului: ")
        return creeaza_disciplina(nume_disc, profesor_disc, lista_disc)
    except ValueError as er:
        print(er)
        return citeste_disc(lista_disc)


def citeste_id(lista, err):
    """

    :param lista: lista cu studentii sau disciplinele
    :param err: mesajul de eroare, in cazul in care id ul citit nu e valid
    :return: id valid(ce se gaseste in lista)
    """
    try:
        _id = int(input("Introduceti un id: "))
        for elem in lista:
            if elem.get_id() == _id:
                return _id
        # ELSE
        print(err)
        return citeste_id(lista, err)
    except ValueError as ex:
        print(ex)
        return citeste_id(lista, err)




def comanda_valida(comanda):
    """
    verifica daca comanda este una din cele valabile
    """
    if not (comanda >=1 and comanda<=8):
        raise ValueError("Nu exista comanda")
def get_comanda():
    """
    se citeste si returneaza o comanda valida

    """
    try:
        comanda=int(input("Introduceti comanda: "))
        comanda_valida(comanda)
    except ValueError as ex:
        print(ex)
        return get_comanda()
    return comanda
def afisare_student(student):
    """afisarea pe ecran a unui student"""
    print("id:",student.get_id(),", nume:",student.get_nume(),end="")
def afisare_disciplina(disc):
    """ afisarea pe ecran a unei discipline"""
    print("id:",disc.get_id(),", nume:",disc.get_nume(),", profesor:",disc.get_profesor(),end="")
def afisare_lista_stud(lista):
    """afisarea listei de studenti"""
    for stud in lista:
        afisare_student(stud)
        print(end="\n")
    print("\n")
def afisare_lista_disc(lista):
    """afisarea listei de discipline"""
    for disc in lista:
        afisare_disciplina(disc)
        print(end="\n")
    print("\n")


def afiseaza_comenzi():
    """afisarea comenzilor"""
    cmd="1.Adauga student\n"
    cmd+="2.Sterge student\n"
    cmd+="3.Adauga disciplina\n"
    cmd+="4.Sterge disciplina\n"
    cmd+="5.Modifica numele studentului cu un anumit id\n"
    cmd+="6.Modifica numele disciplinei cu un anumit id\n"
    cmd+="7.Modifica profesorul disciplinei cu un anumit id\n"
    cmd+="8.Exit"
    print(cmd)

def run():
    lista_stud = [] #lista de studenti
    lista_disc = []#lista de discipline
    while True:
        afiseaza_comenzi()
        comanda = get_comanda()
        if comanda == 1:
            student_nou = citeste_student(lista_stud)
            lista_stud = adauga_student(lista_stud,student_nou)
            afisare_lista_stud(lista_stud)
        elif comanda == 2:
            err = "Nu exista student cu acest ID"
            _id = citeste_id(lista_stud, err)
            lista_stud = sterge_student(lista_stud, _id)
            afisare_lista_stud(lista_stud)
        elif comanda == 3:
            disc_noua=citeste_disc(lista_disc)
            lista_disc = adauga_disc(lista_disc,disc_noua)
            afisare_lista_disc(lista_disc)
        elif comanda == 4:
            err = "Nu exista disciplina cu acest ID"
            _id = citeste_id(lista_disc, err)
            lista_disc = sterge_disciplina(lista_disc, _id)
            afisare_lista_disc(lista_disc)
        elif comanda == 5:
            err = "Nu exista student cu acest ID"
            _id = citeste_id(lista_stud, err)
            nume = citeste_nume("Introduceti noul nume a studentului: ")
            lista_stud = modifica_nume(lista_stud, _id, nume)
            afisare_lista_stud(lista_stud)
        elif comanda == 6:
            err = "Nu exista disciplina cu acest ID"
            _id = citeste_id(lista_disc, err)
            nume = citeste_nume("Introduceti noul nume a disciplinei: ")
            lista_disc = modifica_nume(lista_disc, _id, nume)
            afisare_lista_disc(lista_disc)
        elif comanda == 7:
            err = "Nu exista disciplina cu acest ID"
            _id = citeste_id(lista_disc, err)
            try:
                profesor = citeste_nume("Introduceti noul profesor a disciplinei: ")
                lista_disc = modifica_profesor(lista_disc, _id, profesor)
                afisare_lista_disc(lista_disc)
            except ValueError as er:
                print(er)

        elif comanda == 8:
            exit(0)



#lista=[(Student(15,"ion i"))]
#lista.append(Student(69,"paise"))
#afisare_lista_stud(lista)