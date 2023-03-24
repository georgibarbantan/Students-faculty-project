
from domain.student import Student



class ServiceStudenti:

    def __init__(self, validator_student, repo_studenti):
        """
        Creeaza un obiect de tip ServiceStudenti
        :param validator_student:
        :param repo_studenti:
        """
        self.__validator_student = validator_student
        self.__repo_studenti = repo_studenti

    def getAll(self):
        """
        Returneaaz lista de studenti
        :return: lisat de studenti, lista
        """
        return self.__repo_studenti.getAll()

    def getSudentByIDService(self, id):
        """
        Returneaza stundentul din lista cu id-ul Id
        :param id: numar natural, id-ul studentului
        :return: studentul cu id-ul id
                value error daca studentul nu a fost gasit
        """
        return self.__repo_studenti.getStudentById(id)

    def adaugaStudentService(self, id, nume, grupa):
        """
        Adauga un student in lista de studenti
        :param id: id-ul studentului, numar natural
        :param nume: numele studentuului, sir de caractere
        :param grupa: grupa studentului, numar natural
        :return: -, daca se adauga studentulul cu succes
                arunca exceptie de tip ValueError daca datele studentului nu sunt corecte
        """
        student = Student(id, nume, grupa)
        self.__validator_student.valideazaStudent(student)
        self.__repo_studenti.adauga(student)

    def stergeStudentService(self, id):
        """
        Sterge un student dupa id
        :param id: id-ul studentului ce trebuie modificat, nuamr natural
        :return:
        """
        student = self.__repo_studenti.getStudentById(id)
        self.__validator_student.valideazaStudent(student)
        self.__repo_studenti.sterge(id)

    def modificaStudentService(self, id, numeNou, grupaNoua):
        """
        Modifica studentul care are id-ul id
        :param id: id-ul studentului care trebuie modificat, nuamr natural
        :param numeNou: noul nume al studentului, sir de caractere
        :param grupaNoua: noua grupa a studentului, numar natural
        :return: -; daca studentul a fost modificat cu succes
        """
        student = self.__repo_studenti.getStudentById(id)
        self.__validator_student.valideazaStudent(student)
        self.__repo_studenti.modifica(id, numeNou, grupaNoua)

    def cautaStudent(self, id):
        """
        Cauta un student dupa id
        :param id: id-ul studentului cautat, numar natural
        :return: studentul cautat, daca exista
                arunca exceptie de tip value error
        """
        return self.__repo_studenti.getStudentById(id)
