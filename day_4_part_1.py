import sys

def citeste_cuvinte(nume_fisier):
    """
    Metoda care citeste fiecare cuvant separat dintr-un fisier dat
    :param nume_fisier: Fisierul din care vrem sa citim separat fiecare cuvant
    :return: Lista cu toate cuvintele din fisier
    """
    with open(file = nume_fisier, mode = "rt", encoding = "utf-8") as fisier:
        lista_cuvinte = []
        for line in fisier.readlines():
            lista_cuvinte += line.split()
    return lista_cuvinte



def afiseaza_cuvinte(lista_cuv):
    for cuv in lista_cuv:
        print(cuv, end = ", ")


def main(nume_fisier):
    lista_cuvinte = citeste_cuvinte(nume_fisier)
    afiseaza_cuvinte(lista_cuvinte)

if __name__ == "__main__":
    print(__name__)
    print(sys.argv[0])
    main(sys.argv[1])

















