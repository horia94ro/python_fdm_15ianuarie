from proiect_poo.CarteFizica import CarteFizica
from proiect_poo.Carte import Carte
from proiect_poo.Membru import Membru
from proiect_poo.Bibliotecar import Bibliotecar
from datetime import datetime

lista_carti = []
lista_membri = []
lista_bibliotecari = []

c1 = Carte("Teoria universala", "Stephen Hawking")
c2 = CarteFizica("Primul Razboi Mondial", "Lucian Boia", "Raft 5", "Humanitas")

flo = Membru("Constantinescu", "Petrus", 18, 1)
b1 = Bibliotecar("Popescu", "Ion", 24, datetime(2018, 12, 10))

lista_carti.append(c1)
lista_carti.append(c2)

# try:
#     flo.imprumuta_carte(c2, b1)
#     print(flo.lista_carti_imprumutate)
#     print(b1.verifica_disponibilitate(c2))
#
#
#     flo.returneaza_carte(c2)
#     print(flo.lista_carti_imprumutate)
#     print(flo.nr_carti_imprumutate)
#     print(b1.verifica_disponibilitate(c2))
# except TypeError as e:
#     print(str(e))

"""
COMENZI: 
1) adauga_carte titlu autor 
2) adauga_carte_fizica titlu autor locatie editura
3) imprumuta_carte titlu nume_bibliotecar nume_membru
4) returneaza_carte titlu
5) adauga_membru nume prenume varsta id
6) adauga_bibliotecar nume prenume varsta an luna zi
7) verifica_disponibilitate titlu autor
8) exit
"""
def get_carte(titlu):
    for carte in lista_carti:
        if carte.titlu == titlu:
            return carte

def get_bibliotecar(nume):
    for bibliotecar in lista_bibliotecari:
        if bibliotecar.nume == nume:
            return bibliotecar

def get_membru(nume):
    for membru in lista_membri:
        if membru.nume == nume:
            return membru


while True:
    line = input("Care este comanda dorita?")
    lista = line.split()
    if lista[0] == "adauga_carte":
        lista_carti.append(Carte(lista[1], lista[2]))
    elif lista[0] == "adauga_carte_fizica":
        c1 = CarteFizica(lista[1], lista[2], lista[3], lista[4])
        lista_carti.append(c1)
    elif lista[0] == "imprumuta_carte":
        titlu = lista[1]
        nume_bibliotecar = lista[2]
        nume_membru = lista[3]

        carte = get_carte(titlu)
        bibliotecar = get_bibliotecar(nume_bibliotecar)
        membru = get_membru(nume_membru)
        membru.imprumuta_carte(carte, bibliotecar)
    elif lista[0] == "adauga_membru":
        nume = lista[1]
        prenume = lista[2]
        varsta = lista[3]
        id = lista[4]
        m = Membru(nume, prenume, varsta, id)
        lista_membri.append(m)
    elif lista[0] == "adauga_bibliotecar":
        nume = lista[1]
        prenume = lista[2]
        varsta = lista[3]
        data_angajare = datetime(int(lista[4]), int(lista[5]), int(lista[6]))
        b = Bibliotecar(nume, prenume, varsta, data_angajare)
        lista_bibliotecari.append(b)
    elif lista[0] == "exit":
        print("Programul se va inchide...")
        break







