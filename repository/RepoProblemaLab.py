
class RepoProblemaLab:
    def __init__(self):
        """
        Creaza un obiect de tip Repository ProblemaLab
        """
        self._lst_probleme = []

    def getAll(self):
        """
        Returneaza lista de probleme
        :return: lista de probleme, de tip lista
        """
        # return self._lst_probleme[:]
        return [str(x) for x in self._lst_probleme]

    def getProblemaById(self, id):
        """
        Returneaza o problema de lab care are un anumit id
        :param id:
        :return:
                for elem in self._lst_probleme:
            if elem.getIdProblema() == id:
                return elem
        raise ValueError("Problema inexistenta!\n")
        """
        for i in range(0, len(self._lst_probleme)):
            probl_curenta = self._lst_probleme[i]
            if probl_curenta.getIdProblema() == id:
                return probl_curenta
        return -1


    def adauga(self, problema):
        """
        Adauga o problema noua in lista
        :param problema: problema noua, de tip ProblemaLab
        :return: -; daca problema este aduagta cu succes
        """
        # if problema in self._lst_probleme:
        # raise ValueError("Problema deja exista in lista!\n")
        for elem in self._lst_probleme:
            if problema.getIdProblema()==elem.getIdProblema():
                raise ValueError("Problema cu acest id deja exista")
        self._lst_probleme.append(problema)

    def sterge(self, id):
        """
        Sterge o problema dupa numarul sau
        :param nr_lab_pb: problema cu labul si problema nr_lab_pb va fi sters
        :return: -; daca s a efectuat stergerea cu succes
        """
        problema = self.getProblemaById(id)
        self._lst_probleme.remove(problema)

    def modifica(self, id, nrLabPbNou, descriereNoua, deadlineNou):
        """
        Modifica o problema care are laboratorul si problema nr_lab_pb
        :param nr_lab_pb: numarul problemei care are nr laboratorului si probleimei dat, tuplu
        :param nrLabPbNou: noul numar de labaorator si problema al problemei, tuplu
        :param descriereNoua: noua descriere a problemei, sir de carcatere
        :param deadlineNou: noul deadline al problemei, de tip data calendaristica
        :return: -; modificarea s a efectuat cu succes
        """
        for elem in self._lst_probleme:
            if elem.getIdProblema() == id:
                elem.setNrLaborator_Problema(nrLabPbNou)
                elem.setDescriereProblema(descriereNoua)
                elem.setDeadlineProblema(deadlineNou)
                return
        raise ValueError("Problema inexistenta!\n")

    def __len__(self):
        """
        Returneaza lungimea listei de probleme
        :return:
        """
        return len(self._lst_probleme)
