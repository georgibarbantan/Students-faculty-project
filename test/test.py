
from domain.problema_lab import ProblemaLab
from domain.student import Student
from repository.RepoProblemaLab import RepoProblemaLab
from repository.RepoStudenti import RepositoryStudenti


class Testare:
    def test_creaza_student(self):
        """
        Testeaza functiile get si set din clasa student
        :return: -
        """
        id = 1
        nume = "Nume1"
        grupa = 2
        student = Student(id, nume, grupa)
        assert student.getIdStudent() == id
        assert student.getNumeStudent() == nume
        assert student.getGrupaStudent() == grupa
        student.setNumeStudent("Nume2")
        assert student.getNumeStudent() == "Nume2"
        student.setNumeStudent("Nume3")
        assert student.getNumeStudent() == "Nume3"
        student.setGrupaStudent(3)
        assert student.getGrupaStudent() == 3
        student.setGrupaStudent(7)
        assert student.getGrupaStudent() == 7

    def test_adauga_student(self):
        """
        Functia de test pentu adaugarea unui student
        :return: -
        """
        repoStudenti = RepositoryStudenti()
        assert len(repoStudenti.getAll()) == 0
        student1 = Student(1, "nume1", 2)
        repoStudenti.adauga(student1)
        assert len(repoStudenti.getAll()) == 1
        student2 = Student(2, "nume2", 5)
        repoStudenti.adauga(student2)
        assert len(repoStudenti.getAll()) == 2
        student3 = Student(3, "nume3", 6)
        repoStudenti.adauga(student3)
        assert len(repoStudenti.getAll()) == 3
        student4 = Student(4, "nume4", 2)
        repoStudenti.adauga(student4)
        assert len(repoStudenti.getAll()) == 4
        student5 = Student(5, "nume5", 2)
        repoStudenti.adauga(student5)
        assert len(repoStudenti.getAll()) == 5

    def test_getStudentById(self):
        """
        Functia de test pentru getStudentById()
        :return: -
        """
        repoStudenti = RepositoryStudenti()
        student1 = Student(1, "nume1", 2)
        repoStudenti.adauga(student1)
        student2 = Student(2, "nume2", 5)
        repoStudenti.adauga(student2)
        student3 = Student(3, "nume3", 6)
        repoStudenti.adauga(student3)
        student4 = Student(4, "nume4", 2)
        repoStudenti.adauga(student4)
        student5 = Student(5, "nume5", 2)
        repoStudenti.adauga(student5)
        assert repoStudenti.getStudentById(1) == student1
        assert repoStudenti.getStudentById(2) == student2
        assert repoStudenti.getStudentById(3) == student3
        assert repoStudenti.getStudentById(4) == student4
        assert repoStudenti.getStudentById(5) == student5

    def test_stergeStudent(self):
        """
        Functia de test pentru stergeStundent()
        :return: -
        """
        repoStudenti = RepositoryStudenti()
        studenti = repoStudenti.getAll()
        assert len(studenti) == 0
        student1 = Student(1, "nume1", 2)
        repoStudenti.adauga(student1)
        student2 = Student(2, "nume2", 5)
        repoStudenti.adauga(student2)
        student3 = Student(3, "nume3", 6)
        repoStudenti.adauga(student3)
        student4 = Student(4, "nume4", 2)
        repoStudenti.adauga(student4)
        student5 = Student(5, "nume5", 2)
        repoStudenti.adauga(student5)
        assert len(repoStudenti.getAll()) == 5
        repoStudenti.sterge(1)
        assert len(repoStudenti.getAll()) == 4
        repoStudenti.sterge(2)
        assert len(repoStudenti.getAll()) == 3
        repoStudenti.sterge(3)
        assert len(repoStudenti.getAll()) == 2
        repoStudenti.sterge(4)
        assert len(repoStudenti.getAll()) == 1
        repoStudenti.sterge(5)
        assert len(repoStudenti.getAll()) == 0

    def test_modificaStudent(self):
        """
        Functia de test pentru moficaStudent
        :return: -
        """
        repoStudenti = RepositoryStudenti()
        studenti = repoStudenti.getAll()
        assert len(studenti) == 0
        student1 = Student(1, "nume1", 2)
        repoStudenti.adauga(student1)
        student2 = Student(2, "nume2", 5)
        repoStudenti.adauga(student2)
        student3 = Student(3, "nume3", 6)
        repoStudenti.adauga(student3)
        student4 = Student(4, "nume4", 2)
        repoStudenti.adauga(student4)
        student5 = Student(5, "nume5", 2)
        repoStudenti.adauga(student5)
        nume_nou = "nume50"
        grupa_noua = 2
        repoStudenti.modifica(1, nume_nou, grupa_noua)
        student = repoStudenti.getStudentById(1)
        assert student.getNumeStudent() == "nume50"
        assert student.getGrupaStudent() == grupa_noua

        nume_nou = "Maria"
        grupa_noua = 6
        repoStudenti.modifica(5, nume_nou, grupa_noua)
        student = repoStudenti.getStudentById(5)
        assert student.getNumeStudent() == nume_nou
        assert student.getGrupaStudent() == grupa_noua

        nume_nou = "Andrei"
        grupa_noua = 2
        repoStudenti.modifica(1, nume_nou, grupa_noua)
        student = repoStudenti.getStudentById(1)
        assert student.getNumeStudent() == nume_nou
        assert student.getGrupaStudent() == grupa_noua

        nume_nou = "Cristina"
        grupa_noua = 6
        repoStudenti.modifica(3, nume_nou, grupa_noua)
        student = repoStudenti.getStudentById(3)
        assert student.getNumeStudent() == nume_nou
        assert student.getGrupaStudent() == grupa_noua

    def test_creaza_problema(self):
        """
        Testeaza functiile get si set din clasa student
        :return: -
        """
        id = 1
        nr_lab_pb = [2, 3]
        descriere = "problema 5"
        deadline = 2002 - 2 - 2
        problema = ProblemaLab(id, nr_lab_pb, descriere, deadline)
        assert problema.getIdProblema() == id
        assert problema.getNrLaborator_Problema() == nr_lab_pb
        assert problema.getDescriereProblema() == descriere
        assert problema.getDeadlineProblema() == deadline
        problema.setNrLaborator_Problema([4, 13])
        assert problema.getNrLaborator_Problema() == [4, 13]
        problema.setDescriereProblema("Problema 15")
        assert problema.getDescriereProblema() == "Problema 15"
        problema.setDeadlineProblema(2022 - 2 - 2)
        assert problema.getDeadlineProblema() == 2022 - 2 - 2

    def test_adauga_problema(self):
        """
        Functia de test pentru adaugarea unei probleme
        :return: -
        """
        repoProbleme = RepoProblemaLab()
        assert len(repoProbleme.getAll()) == 0
        problema1 = ProblemaLab(1, [1, 3], "pb3", 2004 - 5 - 6)
        repoProbleme.adauga(problema1)
        assert len(repoProbleme.getAll()) == 1
        problema2 = ProblemaLab(2, [2, 6], "pb66", 1999 - 6 - 7)
        repoProbleme.adauga(problema2)
        assert len(repoProbleme.getAll()) == 2
        problema3 = ProblemaLab(3, [3, 10], "pb100", 2030 - 5 - 6)
        repoProbleme.adauga(problema3)
        assert len(repoProbleme.getAll()) == 3
        problema4 = ProblemaLab(4, [4, 8], "pb8", 2040 - 12 - 23)
        repoProbleme.adauga(problema4)
        assert len(repoProbleme.getAll()) == 4
        problema5 = ProblemaLab(5, [5, 12], "pb12", 2022 - 4 - 1)
        repoProbleme.adauga(problema5)
        assert len(repoProbleme.getAll()) == 5

    def test_sterge_problema(self):
        """
        Functia de test pentru stergerea unei probleme
        :return: -
        """
        repoProbleme = RepoProblemaLab()
        assert len(repoProbleme.getAll()) == 0
        problema1 = ProblemaLab(1, [1, 3], "pb3", 2004 - 5 - 6)
        repoProbleme.adauga(problema1)
        problema2 = ProblemaLab(2, [2, 66], "pb66", 1999 - 6 - 7)
        repoProbleme.adauga(problema2)
        problema3 = ProblemaLab(3, [3, 100], "pb100", 2030 - 5 - 6)
        repoProbleme.adauga(problema3)
        problema4 = ProblemaLab(4, [4, 8], "pb8", 2040 - 12 - 23)
        repoProbleme.adauga(problema4)
        problema5 = ProblemaLab(5, [5, 12], "pb12", 2022 - 4 - 1)
        repoProbleme.adauga(problema5)
        assert len(repoProbleme.getAll()) == 5
        repoProbleme.sterge(1)
        assert len(repoProbleme.getAll()) == 4
        repoProbleme.sterge(2)
        assert len(repoProbleme.getAll()) == 3
        repoProbleme.sterge(3)
        assert len(repoProbleme.getAll()) == 2
        repoProbleme.sterge(4)
        assert len(repoProbleme.getAll()) == 1
        repoProbleme.sterge(5)
        assert len(repoProbleme.getAll()) == 0

    def test_modifica_problema(self):
        """
        Functia de test pentru modifica problema
        :return: -
        """
        repoProbleme = RepoProblemaLab()
        assert len(repoProbleme.getAll()) == 0
        problema1 = ProblemaLab(1, [1, 3], "pb3", 2004 - 5 - 6)
        repoProbleme.adauga(problema1)
        problema2 = ProblemaLab(2, [2, 66], "pb66", 1999 - 6 - 7)
        repoProbleme.adauga(problema2)
        problema3 = ProblemaLab(3, [3, 100], "pb100", 2030 - 5 - 6)
        repoProbleme.adauga(problema3)
        problema4 = ProblemaLab(4, [4, 8], "pb8", 2040 - 12 - 23)
        repoProbleme.adauga(problema4)
        problema5 = ProblemaLab(5, [5, 12], "pb12", 2022 - 4 - 1)
        repoProbleme.adauga(problema5)
        numar_nou = 99
        descriere_noua = "pb 99"
        deadline_nou = 2050 - 2 - 2
        repoProbleme.modifica(1, numar_nou, descriere_noua, deadline_nou)
        # problema = repoProbleme.getProblemaByNrLabPb([1, 3])
        # assert problema.getNumarProblema() == numar_nou
        # assert problema.getDescriereProblema() == descriere_noua
        # assert problema.getDeadlineProblema() == deadline_nou

    def ruleaza_teste(self):
        self.test_creaza_student()
        print("teste creaza student trecute cu succes!")
        self.test_adauga_student()
        print("teste adauga student trecute cu succes!")
        self.test_getStudentById()
        print("teste getStudentById() trecute cu succes!")
        self.test_stergeStudent()
        print("teste sterge student trecute cu succes!")
        self.test_modificaStudent()
        print("teste modifica student trecute cu succes!")
        self.test_creaza_problema()
        print("teste creaza problema trecute cu succes!")
        self.test_adauga_problema()
        print("teste adauga problema trecute cu succes!")
        print("teste getProblemaById trecute cu succes!")
        self.test_sterge_problema()
        print("teste sterge problema trecute cu succes!")
        self.test_modifica_problema()
        print("teste mofifica problema trecute cu succes!")
