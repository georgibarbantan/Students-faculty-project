
class ValidatorStudent:
    def valideazaStudent(self, student):
        """
        Valideaza un student
        :param student: un obiect de tip student
        :return: eroare daca datele sunt incorecte
        """
        errors = ""
        if student.getIdStudent() < 0:
            errors += "Id-ul studentului este invalid!\n"
        if len(student.getNumeStudent()) <= 0:
            errors += "Numele studentului este invslid!\n"
        if student.getGrupaStudent() <= 0:
            errors += "Grupa studentului este invalida!\n"
        if len(errors) > 0:
            raise ValueError(errors)
