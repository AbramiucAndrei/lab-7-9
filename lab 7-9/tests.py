from controller import *
from repository import *


def teste():
    # TESTE controller
    def test_get_maxID(test_stud_list):
        assert get_maxID(test_stud_list)==6

    def test_creeaza_student(test_stud_list):
        stud_nou=creeaza_student("Ioan",test_stud_list)
        assert stud_nou.get_id()==7
        assert stud_nou.get_nume()=="Ioan"

    def test_creeaza_disciplina():
        test_disc_list=[]
        test_disc_list.append(Disciplina(1,"Ion","Matematica"))
        test_disc_list.append(Disciplina(2,"Marius","Romana"))
        test_disc_list.append(Disciplina(3,"George","Engleza"))
        test_disc_list.append(Disciplina(4,"Mihai Popinciuc","Educatie Fizica"))
        disc_noua=creeaza_disciplina("Analiza","Marian Ioan",test_disc_list)
        assert disc_noua.get_id()==5
        assert disc_noua.get_nume()=="Analiza"
        assert disc_noua.get_profesor()=="Marian Ioan"

    test_stud_list=[]
    test_stud_list.append(Student(1,"Andrei Pop"))
    test_stud_list.append(Student(2,"Andrei Muresan"))
    test_stud_list.append(Student(3,"Ioana Zen"))
    test_stud_list.append(Student(6,"Mihai Popescu"))

    test_get_maxID(test_stud_list)
    test_creeaza_student(test_stud_list)
    test_creeaza_disciplina()

    #####TESTE repo####
    def test_adauga_student():
        lista=[]
        lista.append(Student(1,"Ioan"))
        lista=adauga_student(lista,Student(2,"Mihai"))
        assert len(lista)==2
        assert lista[1].get_id()==2
        assert lista[1].get_nume()=="Mihai"
    def test_adauga_disc():
        lista=[]
        lista.append(Disciplina(1,"Marian Marginean","Engleza"))
        lista=adauga_disc(lista,Disciplina(2,"Marcel","Matematica"))
        assert len(lista)==2
        assert lista[1].get_id()==2
        assert lista[1].get_nume()=="Matematica"
        assert lista[1].get_profesor()=="Marcel"

    def test_sterge_disciplina():
        lista = []
        lista.append(Disciplina(1, "Marian Marginean", "Engleza"))
        lista.append(Disciplina(2, "Marcel", "Matematica"))
        lista=sterge_disciplina(lista,1)
        assert len(lista)==1
        assert lista[0].get_id()==2
        assert lista[0].get_nume()=="Matematica"
        assert lista[0].get_profesor()=="Marcel"

    def test_sterge_student():
        lista = []
        lista.append(Student(1, "Ioan"))
        lista.append(Student(2, "Mihai"))
        lista=sterge_student(lista,1)
        assert len(lista) == 1
        assert lista[0].get_id() == 2
        assert lista[0].get_nume() == "Mihai"
    def test_modifica_nume():
        lista = []
        lista.append(Student(1, "Ioan"))
        lista.append(Student(2, "Mihai"))
        lista=modifica_nume(lista,1,"Marcel")
        assert len(lista)==2
        assert lista[0].get_nume()=="Marcel"
    def test_modifica_profesor():
        lista = []
        lista.append(Disciplina(1, "Marian Marginean", "Engleza"))
        lista.append(Disciplina(2, "Marcel", "Matematica"))
        lista=modifica_profesor(lista,1,"Mihai Murar")
        assert len(lista)==2
        assert lista[0].get_profesor()=="Mihai Murar"

    test_adauga_student()
    test_adauga_disc()
    test_sterge_disciplina()
    test_sterge_student()
    test_modifica_nume()
    test_modifica_profesor()

teste()