
from domain.nota import Nota


class ServiceNota:
    def __init__(self, repoNote, repoStudenti, repoProbleme, validatorNota):
        """
        Creaza un obiect de tip ServiceNota
        :param repoNote: repository de note, obiect de tip RepositoryNote
        :param repoStudenti: repository de student, obiect de tip RepositoryStudenti
        :param repoProbleme: repository de probleme, obiect de tip RepoProblemaLab
        """
        self.__repoNote = repoNote
        self.__repoStudenti = repoStudenti
        self.__repoProbleme = repoProbleme
        self.__validatorNota = validatorNota

    def getRepo(self):
        """

        :return:
        """
        return self.__repoNote

    def getAll(self):
        """
        Returneaza lista de note
        :return: lisat de note, lisat
        """
        return self.__repoNote.getAll()

    def cautaNota(self, id):
        """
        Returneaza nota care are id-ul id
        :param id: id-ul notei care trebuie returnat, numar natural
        :return: notat cautata, daca exista
                arunca exceptie de tip ValueError, daca nota nu se afla in lista
        """
        return self.__repoNote.getNotaById(id)

    def adaugaNota(self, idNota, idStudent, idProblema, valoare):
        """
        Adaugam o nota la lisat de note
        :param id: id-ul notei care trebuie adaugat, numar natural
        :param idStudent: id-ul studentului carui ii va fi adaugata nota, numar natural
        :param nr_lab_pb: numarul laboaratorului si al problemei la care va fi asignata nota, tuplu
        :param valoare: valoarea notei, numar real
        :return: -; daca se adauga nota cu succes
        """
        nota = Nota(idNota, idStudent, idProblema, valoare)
        #self.__validatorNota.valideazaNota(Nota)
        self.__repoNote.adauga(nota)

    def stergeNota(self, id):
        """
        Sterge o nota dupa id
        :param id: id-ul notei care trebuie stearsa, numar natural
        :return: -; daca nota este stearsa cu succes
                arunca exceptie de tip Value Error daca datele nu sunt valide
        """
        self.__repoNote.sterge(id)

    def modificaNota(self, id, valoareNoua):
        """
        Modifica o nota
        :param id:id-ul notei care trebuie modificat, numar natural
        :param valoareNoua: noua valoare a notei, numar real
        :return: -; daca nota a fost modificata cu succes
        """
        nota = self.__repoNote.getNotaById(id)
        # self.__validatorNota.valideazaNota(nota)
        self.__repoNote.modifica(id, valoareNoua)


    def lista_studenti_ordonati_problema(self, id_problema):
        """
        Ordoneaza alfabetic dupa nume, dupa nota, lista de studenti si a notelor lor la o problema de laborator data
        :return: lista cu numele studentilor si nota lor la problema si laboratorul respectiv, ordonta crescator

        """

        pb = self.__repoProbleme.getProblemaById(id_problema)
        if pb == -1:
            raise KeyError("Problema cu acest id nu exista!")
        else:
            dictionar_student_note = self.get_studenti_cu_note(id_problema)
            # in functia predefinita sorted() d[0] se refera la "NumeStudent", iar d[1] se refera la nota_student
            dictionar_sortat = sorted(dictionar_student_note.items(), key=lambda d: (d[1], d[0]))
            return dictionar_sortat

    def get_studenti_cu_note(self, id_problema):
        '''
        Metoda ce returneaza un dictionar care mapeaza numele studentului si nota obtinuta la disciplina cu id-ul dat
        :param id_disciplina: id-ul disciplinei cautate
        :return: un dictionar care mapeaza numele studentului si nota obtinuta la disciplina cu id-ul dat
        '''
        # vom salva intr-un dictionar numele si nota fiecarui student, ex: {nume_student1: nota_student1, nume_student2: nota_student2, ...}
        dictionar_student_nota = {}  # in acest dictionar cheile vor fi numele studentilor, iar valorile vor fi notele
        probl_lab = self.__repoNote.getAll()
        for probl in probl_lab:
            if probl.getIdProblemaLab() == id_problema:
                student_id = probl.getIdStudent()
                student = self.__repoStudenti.getStudentById(student_id)  # in student_repository, cautam obiectul student cu acel id si il returnam
                nume_student = student.getNumeStudent()  # am avut nevoie de obiectul student, ca sa putem lua numele studentului
                nota = probl.getValoareNota()
                dictionar_student_nota[nume_student] = nota  # adaugam in dictionar la cheia aferenta numelui studentului, nota lui la problema cautata

        return dictionar_student_nota


    def media_notelor_sub_5(self):
        """
        Toți studenții cu media notelor de laborator mai mic decât 5. (nume student și notă)
        :return: afiseaza studetnii care indeplinesc cerinta data
        """
        n = len(self.__repoNote.getAll())
        lista = self.__repoNote.getAll()
        picati = []
        for i in range(len(lista)):
            idStudent1 = lista[i].getIdStudent()
            if idStudent1 not in picati:
                s = 0
                k = 0
                for j in range(len(lista)):
                    idStudent2 = lista[j].getIdStudent()
                    if idStudent1 == idStudent2:
                        s = s + lista[j].getValoareNota()
                        k = k + 1
                if k > 0:
                    s = s / k
                    picati.append(idStudent1)
                    if s < 5:
                        print(self.__repoStudenti.getStudentById(idStudent1))
                        print("Nota: ")
                        print(s)

    def studentul_cu_cea_mai_mare_medie(self):
        """
        Afiseaza studnetul cu cea mai mare medie
        :return: un obiect de tip student si media acestuia
        """
        n = len(self.__repoNote.getAll())
        lista = self.__repoNote.getAll()
        verificati = []
        media_max = 1
        idStudent = lista[0].getIdStudent()
        salveaza_student = self.__repoStudenti.getStudentById(idStudent)
        for i in range(len(lista)):
            idStudent1 = lista[i].getIdStudent()
            if idStudent1 not in verificati:
                s = 0
                k = 0
                for j in range(len(lista)):
                    idStudent2 = lista[j].getIdStudent()
                    if idStudent1 == idStudent2:
                        s = s + lista[j].getValoareNota()
                        k = k + 1
                if k > 0:
                    s = s / k
                    verificati.append(idStudent1)
                    if s > media_max:
                        media_max = s
                        salveaza_student = self.__repoStudenti.getStudentById(idStudent1)
        return salveaza_student
