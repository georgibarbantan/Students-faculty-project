class Student:
    def __init__(self, idStudent, numeStudent, grupaStudent):
        """
        Creaza un obiect de tipul Student
        :param idStudent: id-ul studentului, numar natura
        :param numeStudent: numele studentului, sir de caractere
        :param grupaStudent: grupa studentului, numar natural
        """
        self.__idStudent = idStudent
        self.__numeStudent = numeStudent
        self.__grupaStudent = grupaStudent

    def getIdStudent(self):
        """
        Returneaza id-ul studentului
        :return: id-ul studentului, nuamr natural
        """
        return self.__idStudent

    def getNumeStudent(self):
        """
        Retruneaza numele studentului
        :return: numele studentului, sir de caractere
        """
        return self.__numeStudent

    def getGrupaStudent(self):
        """
        Returneaza grupa studentului
        :return: grupa studentului, numar natural
        """
        return self.__grupaStudent

    def setNumeStudent(self, numeStudentNou):
        """
        Modifica numele studentului
        :param numeStudentNou: sir de caractere
        :return: -; numele studentului este modificat
        """
        self.__numeStudent = numeStudentNou

    def setGrupaStudent(self, grupaStudentNoua):
        """
        Modifica grupa studentului
        :param grupaStudentNoua: numar natural
        :return: -; grupa studentului este modificata
        """
        self.__grupaStudent = grupaStudentNoua

    def __str__(self):
        """
        Returneaza sirul de caractere aferent studentului
        :return: sirul de caractere aferent studentului
        """
        return "ID student: " + str(self.__idStudent) + ", nume: " + str(
            self.__numeStudent) + ", grupa: " + str(self.__grupaStudent)
