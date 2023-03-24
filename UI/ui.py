
import datetime


class UI:
    def __init__(self, service_studenti, service_probleme, service_note):
        self.__service_studenti = service_studenti
        self.__service_probleme = service_probleme
        self.__service_note = service_note

    def print_meniu(self):
        print("\nMeniu:")
        print("\nSTUDENT")
        print("1. Adauga")
        print("2. Sterge")
        print("3. Modifica")
        print("4. Cauta un student")
        print("5. Returneaza toti studentii din lista")

        print("\nPROBLEMA DE LABORATOR")
        print("6. Adauga")
        print("7. Sterge")
        print("8. Modifica")
        print("9. Cauta o problema de laborator")
        print("10. Returneaza toate problemele din lista")

        print("\nNOTA")
        print("11. Adauga")
        print("12. Sterge")
        print("13. Modifica")
        print("14. Afiseaza toate notele")
        print("15. Sorteaza lista de note")
        print("16. Afiseaza studentii cu media notelor sub 5")
        print("17. Afiseaza studentul cu cea mai mare medie")
        print("\n0. Exit!\n")

    def adauga_student(self):

        id_student = int(input("id: "))
        nume = input("nume: ")
        grupa = int(input("grupa: "))
        try:
            self.__service_studenti.adaugaStudentService(id_student, nume, grupa)
        except ValueError as ve:
            print(ve)

    def sterge_student(self):
        id_student = int(input("id: "))
        try:
            self.__service_studenti.stergeStudentService(id_student)
        except ValueError as ve:
            print(ve)

    def modifica_student(self):
        id_student = int(input("id: "))
        nume = input("nume nou: ")
        grupa = int(input("grupa noua: "))
        try:
            self.__service_studenti.modificaStudentService(id_student, nume, grupa)
        except ValueError as ve:
            print(ve)

    def cauta_student(self):
        id_student = int(input("id: "))
        try:
            print(self.__service_studenti.getSudentByIDService(id_student))
        except ValueError as ve:
            print(ve)

    def afiseaza_studenti(self):
        for student in self.__service_studenti.getAll():
            print(student)

    def adauga_problema(self):
        id_problema = int(input("id: "))
        nr_lab_pb = []
        nr = int(input("nr lab: "))
        nr_lab_pb.append(nr)
        nr = int(input("nr problema: "))
        nr_lab_pb.append(nr)
        descriere = input("descirere: ")
        print("deadline(year, month, day): ")
        y = int(input(""))
        m = int(input(""))
        d = int(input(""))
        deadline = datetime.date(y, m, d)
        try:
            self.__service_probleme.adaugaProblemaService(id_problema, nr_lab_pb, descriere, deadline)
        except ValueError as ve:
            print(ve)

    def sterge_problema(self):
        id_problema = int(input("id: "))
        try:
            self.__service_probleme.stergeProblemaService(id_problema)
        except ValueError as ve:
            print(ve)

    def modifica_problema(self):
        id_problema = int(input("id: "))
        print("se introduc datele noi ale problemei:\n")
        nr_lab_pb_Nou = []
        nr = int(input("nr lab: "))
        nr_lab_pb_Nou.append(nr)
        nr = int(input("nr problema: "))
        nr_lab_pb_Nou.append(nr)
        descriere = input("descirere noua: ")
        print("deadline nou(year, month, day):")
        y = int(input())
        m = int(input())
        d = int(input())
        deadline = datetime.date(y, m, d)
        try:
            self.__service_probleme.modificaProblemaService(id_problema, nr_lab_pb_Nou, descriere, deadline)
        except ValueError as ve:
            print(ve)

    def cauta_problema(self):
        id_problema = int(input("id: "))
        try:
            print(self.__service_probleme.getProblemaByIdService(id_problema))
        except ValueError as ve:
            print(ve)

    def afiseaza_toate_problemele(self):
        for problema in self.__service_probleme.getAll():
            print(problema)


    def adauga_nota(self):
        id1 = int(input("id nota: "))
        id2 = int(input("id student: "))
        id3 = int(input("id problema: "))
        val = int(input("valoare nota: "))
        try:
            self.__service_note.adaugaNota(id1, id2, id3, val)
        except ValueError as ve:
            print(ve)

    def sterge_nota(self):
        id1 = int(input("id nota: "))
        try:
            self.__service_note.stergeNota(id1)
        except ValueError as ve:
            print(ve)

    def modifica_nota(self):
        id1 = int(input("id nota: "))
        val = int(input("valoare noua nota: "))
        try:
            self.__service_note.modificaNota(id1, val)
        except ValueError as ve:
            print(ve)

    def afiseaza_toate_notele(self):
        for nota in self.__service_note.getAll():
            print(nota)

    def sortare_note(self, id_problema):
        self.__service_note.lista_studenti_ordonati_problema(id_problema)
        # for nota in self.__service_note.sortNume(id):
        #     print(nota)

    def run(self):
        while True:
            self.print_meniu()
            option = int(input("Optiunea ta este: "))
            if option == 1:
                self.adauga_student()
            elif option == 2:
                self.sterge_student()
            elif option == 3:
                self.modifica_student()
            elif option == 4:
                self.cauta_student()
            elif option == 5:
                self.afiseaza_studenti()
            elif option == 6:
                self.adauga_problema()
            elif option == 7:
                self.sterge_problema()
            elif option == 8:
                self.modifica_problema()
            elif option == 9:
                self.cauta_problema()
            elif option == 10:
                self.afiseaza_toate_problemele()
            elif option == 11:
                self.adauga_nota()
            elif option == 12:
                self.sterge_nota()
            elif option == 13:
                self.modifica_nota()
            elif option == 14:
                self.afiseaza_toate_notele()
            elif option == 15:
                id_problema = int(input("Introduceti id-ul problemei pentru care doriti sa creati statistica: "))
                print(self.__service_note.lista_studenti_ordonati_problema(id_problema))
            elif option == 16:
                self.__service_note.media_notelor_sub_5()
            elif option == 17:
                print(self.__service_note.studentul_cu_cea_mai_mare_medie())
            elif option == 0:
                print("Programul s-a oprit!")
                return
            else:
                print("Optiune invalida! Introduceti alta comanda!")
