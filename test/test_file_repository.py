from domain.student import Student
from repository.FileRepoStudenti import FileRepositoryStudenti


class Teste:
    def ruleaza_teste(self):
        self.run_file_repo_tests()

    def goleste_fisier(self, nume_fisier):
        with open(nume_fisier, "w") as f:
            pass

    def run_file_repo_tests(self):
        pass
        # nume_fisier = "Testare/studenti_test.txt"
        # self.goleste_fisier(nume_fisier)
        # repo = FileRepositoryStudenti(nume_fisier)
        # assert repo.__len__() == 0
        # student = Student(1, "nume1", 4)
        # repo.adauga(student)
        # assert repo.__len__() == 1
