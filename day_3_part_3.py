fisier = open(file = "exemplu_1.txt", mode = "wt", encoding="utf-8")
fisier.write("Aceasta este prima mea linie")
fisier.write(" acest text este tot pe prima linie\n")
fisier.write("Acest text este totusi pe linia a doua")
fisier.close()

fisier_2 = open(file = "exemplu_1.txt", mode = "rt", encoding="utf-8")
# print(fisier_2.read(8))
# print(fisier_2.tell()) #Pentru a afla indexul pe care se afla cursorul in cadrul fisierului


# fisier_2.seek(24)
#
#
# print(fisier_2.read())
# print(fisier_2.readline())
# print(fisier_2.readlines())
# fisier_2.close()
#
# fisier_nou = open(file = "exemplu_2.txt", mode = "at", encoding="utf-8")
# fisier_nou.writelines(['text de pe prima linie\n', 'urmatoarea linie\n', 'ultima'])
# fisier_nou.close()

# fisier = open(file = "fisier_inexistent.txt")
# fisier.read()
# fisier.close() Va fi aruncata o exceptie in cazul in care fisierul nu exista


# with open(file = "exemplu_2.txt", mode = "rt", encoding = "utf-8") as file:
#     lines = file.readlines()
#
# for line in lines:
#     print(line, end = "")

# nume_fisier = "exemplu_3.txt"
# with open(file = nume_fisier, mode = "wt", encoding = "utf-8") as fisier:
#     fisier.writelines(['linia 1\n', 'linia 2\n', 'linia 3\n'])
#
# with open(file = nume_fisier, mode = "a") as fisier:
#     fisier.writelines(['linia 4\n', 'linia 5'])
#
# with open(file = nume_fisier, mode = 'r') as fisier:
#     lines = fisier.readlines()
#
# print(lines)
# for line in lines:
#     print(line, end = "")

def functie_citire(nume_fisier):
    with open(file = nume_fisier, mode = "rt", encoding = "utf-8") as fisier:
        lines = fisier.readlines()
        lista_cuvinte = []
        for line in lines:

            lista_cuvinte += line.split()

    for cuv in lista_cuvinte:
        print(cuv)

def functie_citire_v2(nume_fisier):
    with open(file=nume_fisier, mode="rt", encoding="utf-8") as fisier:
        var1 = fisier.read()
        var2 = str.replace(var1, ' ', '\n')
        print(var2)

functie_citire_v2("my_file.txt")


