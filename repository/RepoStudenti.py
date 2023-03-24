
class RepositoryStudenti:
    def __init__(self):
        """
        Creaza un obiect de tip RepositoryStudenti
        detine lista de studenti
        """
        self._lst_studenti = list()

    def getAll(self):
        """
        Returneaza lista de studenti
        :return: lista de studenti, de tip lista
        """
        return [x for x in self._lst_studenti]

    def getStudentById(self, idStudent):
        """
        Retruneaza un student in functie de id
        :param idStudent: id0ul studnetului cautat, numar natural
        :return: studentul cautat, daca exista in lista de studenti
        """
        for i in range(0, len(self._lst_studenti)):
            student_curent = self._lst_studenti[i]
            if student_curent.getIdStudent() == idStudent:
                return student_curent
        return -1

    def adauga(self, student):
        """
        Adauga un student in lista de studenti
        :param student: studentul dat
        :return:-; daca studentul este adaugat cu succes
                arunca exceptie daca studentul se afla deja in lista
        """
        for elem in self._lst_studenti:
            if student.getIdStudent()==elem.getIdStudent():
                raise ValueError("Student existent!\n")
        self._lst_studenti.append(student)

    def sterge(self, id):
        """
        Sterge un student din lista de studenti
        :param id: id-ul studentului ce va fi sters
        :return: -
        """
        student = self.getStudentById(id)
        self._lst_studenti.remove(student)

    def modifica(self, id, numeNou, grupaNoua):
        """
        Modifica numele si grupa unui student din lista care are id-ul id
        :param id: id-ul studentului car etrebuie modificta, numar natural
        :param numeNou: numele nou al studentului, de tip sir de caractere
        :param grupaNoua: grupa noua a studentului, de tip numar natural
        :return: -; daca studentula  fost modificat cu succes
        """
        for elem in self._lst_studenti:
            if elem.getIdStudent() == id:
                elem.setNumeStudent(numeNou)
                elem.setGrupaStudent(grupaNoua)
                return
        raise ValueError("Student inexistent!\n")

    def __len__(self):
        """
        Returneaza lungimea listei de studenti
        :return: nr de studenti din lista
        """
        return len(self._lst_studenti)
