
class RepositoryNote:
    def __init__(self):
        """
        Creeazza un obiect de tip RepositoryNote (detine lista de note)
        """
        self._note = []

    def getAll(self):
        """
        Returneaza lisat de note
        :return: lista de note, lista
        """
        return self._note

    def getNotaById(self, id):
        """
        Returneaza o nota in functie de id
        :param id: id-ul notei, numar natural
        :return: nota care are id-ul dat, daca exista
                arunca exceptie
                for nota in self._note:
            if nota.getIdNota() == id:
                return nota
        raise ValueError("Nota inexistenta!\n")

        """
        for i in range(0, len(self._note)):
            nota_curenta = self._note[i]
            if nota_curenta.getIdNota() == id:
                return i
        return -1

    def adauga(self, nota):
        """
        Adauga o nota in lista de note
        :param nota: nota data, un obiect de tip Nota
        :return: -; daca nota este adaugata cu succes
                    arunca expetie de tip value error cu mesajul "nota existenta"
        """
        for elem in self._note:
            if nota.getIdNota()==elem.getIdNota():
                raise ValueError("Nota cu acest id deja exista\n")
        self._note.append(nota)

    def sterge(self, id):
        """
        Sterge o nota dupa id
        :param id: id-ul notei care trebuie stersa, numar natural
        :return: -; daca nota este stearsa cu succes
        """
        nota = self.getNotaById(id)
        self._note.remove(nota)

    def modifica(self, id, valoareNoua):
        """
        Modifica valoarea notei care are id-ul id
        :param id: id-ul notei care trebuie modificat, numar natural
        :param valoareNoua: noua valoare a notei, nuamr real
        :return: -; daca nota este modificata cu succes
        """
        for nota in self._note:
            if nota.getIdNota() == id:
                nota.setValoareNota(valoareNoua)
                return
        raise ValueError("Nota inexistenta!\n")
