from proiect_poo.Persoana import Persoana
from proiect_poo.CarteFizica import CarteFizica


class Membru(Persoana):

    def __init__(self, nume, prenume, varsta, id):
        super().__init__(nume, prenume, varsta)
        self.id = id
        self.nr_carti_imprumutate = 0
        self.lista_carti_imprumutate = []


    def imprumuta_carte(self, carte, bibliotecar):
        if isinstance(carte, CarteFizica):
            if bibliotecar.verifica_disponibilitate(carte):
                self.nr_carti_imprumutate += 1
                self.lista_carti_imprumutate.append(carte)
                carte.imprumutata = True
        else:
            raise TypeError("Cartea \"{}\" nu este fizica - nu poate fi imprumutata"
                                .format(carte.titlu))

    def returneaza_carte(self, carte):
        if isinstance(carte, CarteFizica):
            self.nr_carti_imprumutate -=1
            carte.imprumutata = False
        else:
            raise TypeError("Cartea nu este fizica - nu poate fi returnata")