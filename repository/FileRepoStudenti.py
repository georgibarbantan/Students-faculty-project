
from domain.student import Student
from repository.RepoStudenti import RepositoryStudenti


class FileRepositoryStudenti(RepositoryStudenti):
    def __init__(self, numeFisier):
        """
        Creaza un obiect de tip FileRepositoryStudent
        :param numeFisier: numele fisierului, sir de caractere
        """
        RepositoryStudenti.__init__(self)
        self.__numeFisier = numeFisier

    def __read_all_from_file(self):
        with open(self.__numeFisier, "r") as f:
            lines = f.readlines()
            self._lst_studenti.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id_student = int(parts[0].strip())
                    nume = parts[1].strip()
                    grupa = int(parts[2].strip())
                    student = Student(id_student, nume, grupa)
                    self._lst_studenti.append(student)
        return self._lst_studenti

    def __write_all_to_file(self):
        with open(self.__numeFisier, "w") as f:
            for student in self._lst_studenti:
                f.write(str(student.getIdStudent()) + "," + student.getNumeStudent() + "," + str(
                     student.getGrupaStudent()) + "\n")

    def adauga(self, student):
        """
        Adauga un studet in fisier
        :param student: studetnul ce eset adaugat, de tip Student
        :return: -;studentul este adaugat in fisier
        """
        self.__read_all_from_file()
        RepositoryStudenti.adauga(self, student)
        self.__write_all_to_file()

    def sterge(self, id):
        """
        Sterge stdentul care are id-ul id
        :param id: id-ul studnetului, numar natural
        :return: -; daca studentul este sters cu succes
        """
        self.__read_all_from_file()
        RepositoryStudenti.sterge(self, id)
        self.__write_all_to_file()

    def modifica(self, id, numeNou, grupaNoua):
        """
        Modifica un student care are id-ul id
        :param id: idul studentului, numar natural
        :param numeNou: noul nume al studentului, sir de caractere
        :param grupaNoua: noua grupa a studentului, numar natural
        :return: -; daca studentul este modificatc cu succes
        """
        self.__read_all_from_file()
        RepositoryStudenti.modifica(self, id, numeNou, grupaNoua)
        self.__write_all_to_file()

    def getAll(self):
        """
        Returneaza lista de studenti din fisier
        :return: lisat de studenti
        """
        self.__read_all_from_file()
        return RepositoryStudenti.getAll(self)

    def getStudentById(self, idStudent):
        """
           #     Returneaza un student in functie de id
           #     :param idStudent: id- ul studentului care trebuie returnat
           #     :return: studentul cautat
           #     """
        self.__read_all_from_file()
        return RepositoryStudenti.getStudentById(self, idStudent)

    def __len__(self):
        """
        Returneaza lungimea listei de studenti din fisier
        :return: nr de studenti din lista
        """
        self.__read_all_from_file()
        return RepositoryStudenti.__len__(self)
