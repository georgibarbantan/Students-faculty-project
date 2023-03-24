
from domain.problema_lab import ProblemaLab
from repository.RepoProblemaLab import RepoProblemaLab


class FileRepoProblemeLab(RepoProblemaLab):
    def __init__(self, numeFisier):
        """
        Creaza un obiect de tip FileRepoProblemeLab
        :param numeFisier: numele fisierului, sir de caractere
        """
        RepoProblemaLab.__init__(self)
        self.__numeFisier = numeFisier

    def __read_all_from_file(self):
        with open(self.__numeFisier, "r") as f:
            lines = f.readlines()
            self._lst_probleme.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id_problema = int(parts[0].strip())
                    str_lab_pb = parts[1].strip()
                    list_lab_pb = str_lab_pb.split('.')
                    nr_lab_pb = (int(list_lab_pb[0].strip()),int(list_lab_pb[1].strip()))
                    descriere = parts[2].strip()
                    deadline = parts[3].strip()
                    problema = ProblemaLab(id_problema, nr_lab_pb, descriere, deadline)
                    self._lst_probleme.append(problema)
        return self._lst_probleme

    def __write_all_to_file(self):
        with open(self.__numeFisier, "w") as f:
            for problema in self._lst_probleme:
                f.write(str(problema.getIdProblema())+","+str(problema.getNrLaborator_Problema()[0])+'.'+str(problema.getNrLaborator_Problema()[1])+","+\
                        problema.getDescriereProblema()+","+str(problema.getDeadlineProblema()))

    def adauga(self, problema):
        """
        Adauga o problema de laborator in fisierul text
        :param problema: problema care este adaugata, de tip ProblemaLab
        :return: -; problema este adaugata in fisier
        """
        self.__read_all_from_file()
        RepoProblemaLab.adauga(self, problema)
        self.__write_all_to_file()

    def sterge(self, id):
        """
        Sterge din fiserul text o problema de laborator care are id-ul id
        :param id: id-ul problemei care trebui sters, nuamr natuarl
        :return: -; daca id-ul este sters cu succes
        """
        self.__read_all_from_file()
        RepoProblemaLab.sterge(self, id)
        self.__write_all_to_file()

    def modifica(self, id, nrLabPbNou, descriereNoua, deadlineNou):
        """
        Modifica din fiserul text o problema care are id-ul id
        :param id: id-ul problemei care trebuie modificata, numar natural
        :param nrLabPbNou: noul numar al problemei, de tip tuplu (nr laborator, nuamr problema)
        :param descriereNoua: noua descriere a probleemi
        :param deadlineNou: noul deadline al problemei
        :return: -; daca problema este modificata cu succes
        """
        self.__read_all_from_file()
        RepoProblemaLab.modifica(self, id, nrLabPbNou, descriereNoua, deadlineNou)
        self.__write_all_to_file()

    def getAll(self):
        """
        Returneaza lista de probleme din fisier
        :return: lista de probleme din fisier
        """
        self.__read_all_from_file()
        return RepoProblemaLab.getAll(self)

    def getProblemaById(self, id):
        """
        Returneaza din fiserul text oproblema in functie de id-ul dat
        :param id: id-ul problemei care trebuie retrunata
        :return: problema cautata
        """
        self.__read_all_from_file()
        return RepoProblemaLab.getProblemaById(self, id)

    def __len__(self):
        """
        Returneaza lungimea listei de probleme din fisier
        :return: numarul de probleme din fisier
        """
        self.__read_all_from_file()
        RepoProblemaLab.__len__(self)
        self.__write_all_to_file()
