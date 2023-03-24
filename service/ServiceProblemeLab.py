
from domain.problema_lab import ProblemaLab



class ServiceProbleme:
    def __init__(self, validator_problema, repo_probleme):
        """
        Creeaza un obiect de tip ServiceProblema
        :param validator_problema:
        :param repo_probleme:
        """
        self.__validator_problema = validator_problema
        self.__repo_probleme = repo_probleme

    def getAll(self):
        """
        Returneaza lista de probleme
        :return: lista de probleme, lista
        """
        return self.__repo_probleme.getAll()

    def getProblemaByIdService(self, id):
        """
        Returneaza problema care are numarul laboratorului si problema nr_lab_pb, tuplu
        :param nr_lab_pb: tuplu
        :return: problema de laborator
                value error daca problema nu a fost gasita
        """
        return self.__repo_probleme.getProblemaById(id)

    def adaugaProblemaService(self, id, nr_lab_problema, descriere, deadline):
        """
        Adauga o problema in lista de probleme
        :param nr_lab_problema: numarul laboratorului si numarul probblemei,de tip tuplu
        :param descriere: descrierea problemei, sir de carcatere
        :param deadline: deadline-ul problemei, lista de 3
        :return: -; daca problema a fost adaugata cu succes
        """
        problema = ProblemaLab(id, nr_lab_problema, descriere, deadline)
        #self.__validator_problema.valideazaProblema(problema)
        self.__repo_probleme.adauga(problema)

    def stergeProblemaService(self, id):
        """
        Sterge o problema care are un anumit id
        :param nr_lab_pb: numar de laborator si problema al problemei care trebuie sters
        :return: -; daca problema a fost stearsa cu succes
                eroare, altfel
        """
        problema = self.__repo_probleme.getProblemaById(id)
        #self.__validator_problema.valideazaProblema(problema)
        self.__repo_probleme.sterge(id)

    def modificaProblemaService(self, id, nrLabPbNoua, descriereNoua, deadlineNou):
        """
        Modifica problema care are id-ul problema
        :param nr_lab_pb: numarul laboratorlui si al problemi problemei care trebuie modificat
        :param nrLabPbNoua: noul numar de laborator si problema al problemei
        :param descriereNoua: noua descriere a problemei
        :param deadlineNou: noul deadline al problemei
        :return: -; daca modificarea s a efectuat cu succes
                eroare in caz contrar
        """
        problema = self.__repo_probleme.getProblemaById(id)
        #self.__validator_problema.valideazaProblema(problema)
        self.__repo_probleme.modifica(id, nrLabPbNoua, descriereNoua, deadlineNou)

