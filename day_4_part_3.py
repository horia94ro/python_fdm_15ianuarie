#SUBIECTE REZOLVATE TIP PARTIAL

# d = 10
# while d:
#     d = d - 1
#     if d == 5:
#         continue
#     print(d)

# with open(file = "exemplu.txt", mode = "w+") as fisier:
#     fisier.writelines(['examen partial practic \n', 'sustinut la Telecom Academy\n'])
#     fisier.write('linie suplimentara\n')
#     fisier.write('ultima linie')
#     fisier.seek(0)
#     lines = fisier.readlines()
#     print(lines, type(lines))
#####################################################################
def modifica_valoare(x):
    """
    Modificat o valoare de tip immutable (int)
    """
    print("ID-ul lui x la inceputul metodei", id(x))
    x += 1
    print(x)

    print("ID-ul lui x la sfarsitul metodei", id(x))

# a = 10
# print("ID-ul valorii la inceputul progr: ", id(a))
# modifica_valoare(a)
# print("ID-ul valorii la sfarsitul programului", id(a))
# print(a)

def modifica_lista(lista):
    print("ID-ul listei la inceputul metodei: ", id(lista))
    lista.append(10)
    print(lista)
    print("ID-ul listei la sfarsitul metodei: ", id(lista))



# lista = [7, 8, 9]
# print("ID-ul listei la inceputul programului: ", id(lista))
# modifica_lista(lista)
# print("ID-ul listei la sfarsitul programului: ", id(lista))
# print(lista)

def adunare(a, b):
    return a + b



# print(adunare(10, 5))
# print(adunare("Telecom ", "Academy"))
# print(adunare(10.5, 7.2))
# print(adunare([1, 2, 3], [4, 5, 6]))
# print(adunare((1, 2, 3), (7, )))
# print(adunare(10, "Academy")) #Arunca exceptie pentru ca limbajul este strong-typed
import builtins
# print(open is builtins.open) #scope built-in

open = "Un sir de caracter definit global" #scope global
# print(open)

def functia_mea():
    print(open)

def functia_ta():
    open = "sir modificat de caractere"
    print(open)

def functia_lor():
    var = 10
    def f():
        print("Functie imbricata!")
        print(var)
    f()

# functia_lor()
# functia_mea()
#
# functia_ta()
# print(open)
# print(open is builtins.open)

def afiseaza_x():
    print("Valoarea lui x: ", x)


def modifica_x(x_nou):
    global x
    x = x_nou

x = 10
afiseaza_x()
modifica_x(15)
print(x)
#
#
#



