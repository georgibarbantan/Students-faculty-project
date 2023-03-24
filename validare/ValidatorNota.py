
class ValidatorNota:
    def valideazaNota(self, nota):
        """
        Valideaz o nota
        :param nota: nota ce trebuie validata
        :return: -; daca nota este valida
                arunca exceptie de tip ValueError daca datele notei sunt incorecte
        """
        errors = ""
        if nota.getIdNota() < 0:
            errors += "Id-ul notei este invalid!\n"
        if nota.getStudent().getIdStudent() < 0:
            errors += "Id-ul studentului este invalid!\n"
        if nota.getProblemaLab().getProblemaByNrLabPb()[0] < 0:
            errors += "Numarulul laboratorului este invalid!\n"
        if nota.getProblemaLab().getProblemaByNrLabPb()[1] < 0:
            errors += "Numarul problemei este invalid!\n"
        if nota.getValoareNota() < 1 or nota.getValoareNota() > 10:
            errors += "Valoarea notei este invalida!\n"
        if len(errors) > 0:
            raise ValueError(errors)
