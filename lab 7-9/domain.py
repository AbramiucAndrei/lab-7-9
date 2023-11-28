class Student:
    def __init__(self,id,_nume):
        """
        :param id: se primeste id-ul studentului
        :param _nume: se primeste numele studentului
        """
        self.__idStud=id
        self.nume=_nume
    def get_id(self):
        """
        :return: id-ul studentului
        """
        return self.__idStud
    def get_nume(self):
        """
        :return:numele studentului
        """
        return self.nume
    def set_nume(self,nume_nou):
        """
        :param nume_nou: se primeste noul nume al studentului,ce
        va fi inlocuit cu cel vechi
        """
        self.nume=nume_nou

class Disciplina:
    def __init__(self,id,_profesor,_numeDisc):
        """
        :param id: id-ul disciplinei
        :param _profesor: numele profesorului
        :param _numeDisc: numele disciplinei
        """
        self.__idDisc=id
        self.profesor=_profesor
        self.nume=_numeDisc
    def get_id(self):
        """
        :return: id-ul disciplinei
        """
        return self.__idDisc
    def get_profesor(self):
        """
        :return: profesorul disciplinei
        """
        return self.profesor
    def get_nume(self):
        """
        :return: numele disciplinei
        """
        return self.nume
    def set_profesor(self,profesor_nou):
        """
        :param profesor_nou: numele noului profesor de la disciplina "self"
        """
        self.profesor=profesor_nou
        #return self.profesor

    def set_nume(self,nume_nou):
        """
        :param nume_nou: numele nou al disciplinei "self"
        """
        self.nume=nume_nou
        #return self.nume

class ValidationError(Exception):
    """
    clasa de generare de exceptie
    """
    def __init__(self,error):
        self.__error=error
    def getErrors(self):
        return self.__error


class Validate_student:
    """validarea studentului si aruncarea exceptiei daca este cazul"""
    def validate(self, stud):
        errors=[]
        if stud.get_id() == "":
            errors.append("Studentul nu are id!")
        if stud.get_nume() == "":
            errors.append("Studentul nu are nume!")
        if len(errors)>0 : raise ValidationError(errors)

class Validate_disciplina:
    """
    validarea disciplinei is aruncarea exceptiei daca este cazul
    """
    def validate(self, disc):
        errors=[]
        if disc.get_id() == "":
            errors.append("Disciplina nu are id!")
        if disc.get_nume() == "":
            errors.append("Disciplina nu are nume!")
        if disc.get_profesor() == "":
            errors.append("Disciplina nu are profesor!")
        if len(errors)>0 : raise ValidationError(errors)


#TESTE
def test_Validate_student():
    val=Validate_student()

    st=Student("","vasi")
    try:
        val.validate(st)
        assert False
    except ValidationError as ex:
        assert len(ex.getErrors())==1

    st=Student("","")
    try:
        val.validate(st)
        assert False
    except ValidationError as ex:
        assert len(ex.getErrors())==2

def test_Validate_disciplina():
    disc=Disciplina("","","")
    val=Validate_disciplina()

    try:
        val.validate(disc)
        assert False
    except ValidationError as ex:
        assert len(ex.getErrors())==3

    disc=Disciplina("","Dan Popescu","")
    try:
        val.validate(disc)
        assert False
    except ValidationError as ex:
        assert len(ex.getErrors())==2

test_Validate_student()
test_Validate_disciplina()