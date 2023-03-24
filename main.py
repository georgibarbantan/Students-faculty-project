

from repository.FileRepoNote import FileRepositoryNote
from repository.FileRepoProbleme import FileRepoProblemeLab
from repository.FileRepoStudenti import FileRepositoryStudenti
from repository.RepoNote import RepositoryNote
from service.ServiceNote import ServiceNota
from UI.ui import UI
from validare.ValidatorNota import ValidatorNota
from validare.ValidatorProblema import ValidatorProblema
from validare.ValidatorStudent import ValidatorStudent
from repository.RepoStudenti import RepositoryStudenti
from repository.RepoProblemaLab import RepoProblemaLab
from service.ServiceStudenti import ServiceStudenti
from service.ServiceProblemeLab import ServiceProbleme
from test.test import Testare
from test.test_file_repository import Teste
from test.unittests import TestCaseDomeniu, TestCaseRepository

def start():

    #teste = Testare()
    #teste.ruleaza_teste()

    teste = TestCaseDomeniu()
    teste.setUp()
    teste.test_student()
    teste.test_probleme_lab()
    teste.test_nota()
    teste= TestCaseRepository()
    teste.setUp()
    teste.test_repo_studenti()
    teste.test_repo_problema()

    validator_student = ValidatorStudent()
    validator_problema = ValidatorProblema()
    validator_nota = ValidatorNota()
    metoda = input("Introduceti metoda de persistenta(memorie/ fisier): ")
    if metoda == "memorie":
        repo_studenti = RepositoryStudenti()
        repo_probleme = RepoProblemaLab()
        repo_note = RepositoryNote()
    elif metoda == "fisier":
        repo_studenti = FileRepositoryStudenti("studenti.txt")
        repo_probleme = FileRepoProblemeLab("probleme.txt")
        repo_note = FileRepositoryNote("note.txt")
    else:
        print("Metoda de persistenta invalida!")
        return
    service_studenti = ServiceStudenti(validator_student, repo_studenti)
    service_probleme = ServiceProbleme(validator_problema, repo_probleme)
    service_note = ServiceNota(repo_note, repo_studenti, repo_probleme, validator_nota)
    consola = UI(service_studenti, service_probleme, service_note)
    consola.run()


if __name__ == '__main__':
    start()
