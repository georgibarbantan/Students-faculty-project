import unittest

from domain.nota import Nota
from domain.problema_lab import ProblemaLab
from domain.student import Student
from repository.RepoNote import RepositoryNote
from repository.RepoProblemaLab import RepoProblemaLab
from repository.RepoStudenti import RepositoryStudenti
from validare.ValidatorStudent import ValidatorStudent


class TestCaseDomeniu(unittest.TestCase):
    def setUp(self) -> None:
        print("SetUp Domeniu")
        self.__student1 = Student(1, "nume1", 2)
        self.__student2 = Student(2, "nume2", 4)
        self.__student3 = Student(3, "nume3", 7)
        self.__problema1 = ProblemaLab(1, [2, 3], "laborator 2, problema 3", 2023 - 4 - 5)
        self.__problema2 = ProblemaLab(2, [2, 3], "laborator 2, problema 3", 2023 - 4 - 5)
        self.__problema3 = ProblemaLab(3, [5, 6], "laborator 5, problema 6", 2025 - 2 - 12)
        self.__nota1 = Nota(1, 1, 1, 5)
        self.__nota2 = Nota(2, 2, 1, 3)
        self.__nota3 = Nota(3, 3, 1, 2)

    def test_student(self):
        """
        Testeaza functiile din clasa Student
        :return: -
        """
        print("Ruleaza teste student domeniu")
        self.assertEqual(self.__student1.getIdStudent(), 1)
        self.assertEqual(self.__student1.getNumeStudent(), "nume1")
        self.assertEqual(self.__student1.getGrupaStudent(), 2)
        self.__student1.setNumeStudent("nume2")
        self.assertEqual(self.__student1.getNumeStudent(), "nume2")
        self.assertEqual(str(self.__student1), "ID student: 1, nume: nume2, grupa: 2")
        self.__student2.setGrupaStudent(2)
        # self.assertEqual(self.__student1, self.__student2)

    def test_probleme_lab(self):
        """
        Testeaza functiile din clasa ProblemaLab
        :return: -
        """
        print("Ruleaza teste ProblemaLab domeniu")
        self.assertEqual(self.__problema1.getIdProblema(), 1)
        self.assertEqual(self.__problema1.getNrLaborator_Problema(), [2, 3])
        self.assertEqual(self.__problema1.getDescriereProblema(), "laborator 2, problema 3")
        self.assertEqual(self.__problema1.getDeadlineProblema(), 2023 - 4 - 5)
        self.__problema1.setDeadlineProblema(2030 - 5 - 5)
        self.assertEqual(self.__problema1.getDeadlineProblema(), 2030 - 5 - 5)
        self.__problema1.setDescriereProblema("descriere noua")
        self.assertEqual(self.__problema1.getDescriereProblema(), "descriere noua")
        # self.assertEqual(self.__problema1, "Id-ul problemei: 1 Numar laborator si problema: [2,3], descriere: \
        # descriere noua, deadline: 2030-5-5")

    def test_nota(self):
        """
        Testeaza functiile din clasa Nota
        :return: -
        """
        print("Ruleaza teste Nota domeniu")
        self.assertEqual(self.__nota1.getIdNota(), 1)
        self.assertEqual(self.__nota1.getIdStudent(), 1)
        self.assertEqual(self.__nota1.getIdNota(), 1)
        self.assertEqual(self.__nota1.getIdProblemaLab(), 1)
        self.assertEqual(self.__nota1.getValoareNota(), 5)
        self.__nota1.setValoareNota(10)
        self.assertEqual(self.__nota1.getValoareNota(), 10)
        self.assertTrue(self.__nota1.__str__() == "Id nota: " + str(self.__nota1.getIdNota()) + ", Id Student:" + str(self.__nota1.getIdStudent()) + \
               ", id Problema de Laborator: " + str(self.__nota1.getIdProblemaLab()) + ", valoare nota " + str(self.__nota1.getValoareNota()))


class TestCaseRepository(unittest.TestCase):
    def setUp(self) -> None:
        print("ruleaza SetUp")
        self.__repoStudenti = RepositoryStudenti()
        self.__student1 = Student(1, "nume1", 2)
        self.__student2 = Student(2, "nume2", 4)
        self.__student3 = Student(3, "nume3", 7)
        self.__student4 = Student(4, "nume4", 5)
        self.__student5 = Student(5, "nume5", 3)
        self.__student6 = Student(6, "nume6", 1)
        self.__student7 = Student(7, "nume7", 7)

        self.__repoProbleme = RepoProblemaLab()
        self.__problema1 = ProblemaLab(1, [2, 3], "laborator 2, problema 3", 2023 - 4 - 5)
        self.__problema2 = ProblemaLab(2, [2, 3], "laborator 2, problema 3", 2023 - 4 - 5)
        self.__problema3 = ProblemaLab(3, [5, 6], "laborator 5, problema 6", 2025 - 2 - 12)

        self.__repoNote = RepositoryNote()
        self.__nota1 = Nota(1, 1, 1, 5)
        self.__nota2 = Nota(2, 2, 1, 3)
        self.__nota3 = Nota(3, 3, 1, 2)
        self.__nota4 = Nota(4, 4, 1, 9)
        self.__nota5 = Nota(5, 5, 1, 2)
        self.__nota6 = Nota(6, 6, 1, 1)

    def test_repo_studenti(self):
        print("Ruleaza teste Reposotory Studenti")
        # adauga
        repoStudenti = RepositoryStudenti()
        studenti = self.__repoStudenti.getAll()
        self.assertTrue(len(studenti) == 0)
        self.__repoStudenti.adauga(self.__student1)
        studenti = self.__repoStudenti.getAll()
        self.assertTrue(len(studenti) == 1)
        self.__repoStudenti.adauga(self.__student2)
        studenti = self.__repoStudenti.getAll()
        self.assertTrue(len(studenti) == 2)
        self.__repoStudenti.adauga(self.__student3)
        studenti = self.__repoStudenti.getAll()
        self.assertTrue(len(studenti) == 3)
        studenti = self.__repoStudenti.getAll()
        # print(studenti[0].getIdStudent())
        # self.assertTrue(len(studenti) == 4)
        # self.assertTrue(studenti[1].getIdStudent() == 2)
        # self.assertTrue(studenti[1].getNumeStudent() == "nume2")
        # self.assertTrue(studenti[1].getGrupaStudent() == 2)
        # self.assertTrue(studenti[4].getIdStudent() == 4)
        # self.assertTrue(studenti[4].getNumeStudent() == "nume4")
        # self.assertTrue(studenti[4].getGrupaStudent() == 5)

        # getById
        studentCautat1 = self.__repoStudenti.getStudentById(1)
        self.assertTrue(studentCautat1 == self.__student1)
        self.assertTrue(studentCautat1.getIdStudent() == 1)
        # self.assertTrue(studentCautat1.getNumeStudnet() == "nume1")
        studentCautat2 = self.__repoStudenti.getStudentById(2)
        # self.assertTrue(studentCautat2 == self.__student2)

        # stergere
        self.__repoStudenti.sterge(1)
        studenti = self.__repoStudenti.getAll()
        self.assertTrue(len(studenti) == 2)
        # self.assertTrue(self.__repoStudenti.getStudentById(studenti.getIdStudent())==1)
        # self.assertTrue(studenti[])

        # modificare
        self.__repoStudenti.adauga(self.__student4)
        self.__repoStudenti.adauga(self.__student5)
        studenti = self.__repoStudenti.getAll()
        self.assertTrue(len(studenti) == 4)

    def test_repo_problema(self):
        print("Ruleaza teste Repository ProblemaLab")
        # adauga
        probleme = self.__repoProbleme.getAll()
        self.assertTrue(len(probleme) == 0)
        self.__repoProbleme.adauga(self.__problema1)
        self.assertEqual(len(self.__repoProbleme.getAll()), 1)
        self.__repoProbleme.adauga(self.__problema2)
        self.assertEqual(len(self.__repoProbleme.getAll()), 2)
        self.__repoProbleme.adauga(self.__problema3)
        self.assertEqual(len(self.__repoProbleme.getAll()), 3)
        self.assertEqual(self.__repoProbleme.__len__(), 3)
        #self.assertTrue(self.__repoProbleme.adauga(self.__problema1) == "Problema cu acest id deja exista")
        # getById
        self.assertEqual(self.__repoProbleme.getProblemaById(10), -1)
        # sterge
        self.assertTrue(len(self.__repoProbleme.getAll()) == 3)
        self.__repoProbleme.sterge(3)
        self.assertEqual(len(self.__repoProbleme.getAll()), 2)
        self.__repoProbleme.sterge(2)
        self.assertEqual(len(self.__repoProbleme.getAll()), 1)
        self.__repoProbleme.sterge(1)
        self.assertEqual(len(self.__repoProbleme.getAll()), 0)

        # modificare
        #self.__repoProbleme.modifica(10, 5, "a", 2020 - 6 - 4)
        #self.assertTrue((self.__repoProbleme.modifica(10, 5, "a", 2020-6-4)) == "Problema inexistenta!\n")
        self.__repoProbleme.adauga(self.__problema1)
        self.__repoProbleme.adauga(self.__problema2)
        self.__repoProbleme.adauga(self.__problema3)
        self.assertTrue(len(self.__repoProbleme.getAll()) == 3)
        self.__repoProbleme.modifica(2, [5, 6], "descrierenoua", 2030 - 4 - 5)
        problema = self.__repoProbleme.getProblemaById(2)
        self.assertTrue(problema.getIdProblema() == 2)
        self.assertTrue(problema.getNrLaborator_Problema() == [5, 6])
        self.assertTrue(problema.getDescriereProblema() == "descrierenoua")
        self.assertTrue(problema.getDeadlineProblema() == 2030 - 4 - 5)

    def test_repo_note(self):
        print("Ruleaza teste Repository Nota")
        # adauga
        note = self.__repoNote.getAll()
        self.assertTrue(len(note) == 0)
        self.__repoNote.adauga(self.__nota1)
        self.assertEqual(len(self.__repoNote.getAll()), 1)
        self.__repoNote.adauga(self.__nota2)
        self.assertEqual(len(self.__repoNote.getAll()), 2)
        self.__repoNote.adauga(self.__nota3)
        self.assertEqual(len(self.__repoNote.getAll()), 3)
        self.__repoNote.adauga(self.__nota4)
        self.assertEqual(len(self.__repoNote.getAll()), 4)
        self.__repoNote.adauga(self.__nota5)
        self.assertEqual(len(self.__repoNote.getAll()), 5)
        self.__repoNote.adauga(self.__nota6)
        self.assertEqual(len(self.__repoNote.getAll()), 6)
        #self.assertTrue(self.__repoNote.getNotaById(1) == 5)
        #self.assertTrue( self.__repoNote.adauga(self.__nota6) == "Nota cu acest id deja exista\n")
        # stergere
        self.assertEqual(len(self.__repoNote.getAll()), 6)
        #self.__repoNote.sterge(6)
        #self.assertEqual(len(self.__repoNote.getAll()), 5)
        #self.__repoNote.sterge(5)
        #self.assertEqual(len(self.__repoNote.getAll()), 4)
        #self.__repoNote.sterge(4)
        #self.assertEqual(len(self.__repoNote.getAll()), 3)
        #self.__repoNote.sterge(3)
        #self.assertEqual(len(self.__repoNote.getAll()), 2)

        # modifica
        #self.__repoNote.adauga(5)
        #self.__repoNote.adauga(6)
        #self.assertEqual(len(self.__repoNote.getAll()), 4)
        #self.__repoNote.modifica(10, 5)
        #self.assertTrue(self.__repoNote.modifica(10, 5) == "Nota inexistenta!\n")
        #nota = self.__repoNote.getNotaById(1)
        #self.assertTrue(nota.getValoareNota() == 5)
        #self.__repoNote.modifica(2, 8)
        #nota = self.__repoNote.getNotaById(2)
        #self.assertTrue(nota.getValoareNota() == 8)
        # self.__repoNote.modifica(5, 9)
        # nota = self.__repoNote.getNotaById(5)
        # self.assertTrue(nota.getValoareNota() == 9)
        # self.__repoNote.modifica(5, 10)
        # nota = self.__repoNote.getNotaById(5)
        # self.assertTrue(nota.getValoareNota() == 10)


class TestCaseService(unittest.TestCase):
    def setUp(self) -> None:
        self.__validStudent = ValidatorStudent()
        self.__repoStudneti = RepositoryStudenti(self.__repoStudneti, self.__validStudent)


class TestCaseUIfunctions(unittest.TestCase):

    def setUp(self) -> None:
        #self.__functii = UI()

        self.__student1 = Student(1, "nume1", 2)
        self.__student2 = Student(2, "nume2", 4)
        self.__student3 = Student(3, "nume3", 7)
        self.__student4 = Student(4, "nume4", 5)
        self.__student5 = Student(5, "nume5", 3)
        self.__student6 = Student(6, "nume6", 1)
        self.__student7 = Student(7, "nume7", 7)

        self.__problema1 = ProblemaLab(1, [2, 3], "laborator 2, problema 3", 2023 - 4 - 5)
        self.__problema2 = ProblemaLab(2, [2, 3], "laborator 2, problema 3", 2023 - 4 - 5)
        self.__problema3 = ProblemaLab(3, [5, 6], "laborator 5, problema 6", 2025 - 2 - 12)

        self.__nota1 = Nota(1, 1, 1, 5)
        self.__nota2 = Nota(2, 2, 1, 3)
        self.__nota3 = Nota(3, 3, 1, 2)
        self.__nota4 = Nota(4, 4, 1, 9)
        self.__nota5 = Nota(5, 5, 1, 2)
        self.__nota6 = Nota(6, 6, 1, 1)

    def test_sortare(self):
        note_studenti = []
        note_studenti.append(self.__nota1)
        note_studenti.append(self.__nota2)
        note_studenti.append(self.__nota3)
        note_studenti.append(self.__nota4)
        note_studenti.append(self.__nota5)
        note_studenti.append(self.__nota6)
        #self.__functii.sortare_note(note_studenti)
        #self.assertTrue(note_studenti[0] == self.__nota6)

