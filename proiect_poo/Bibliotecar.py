from proiect_poo.Persoana import Persoana
from proiect_poo.CarteFizica import CarteFizica

class Bibliotecar(Persoana):

    def __init__(self, nume, prenume, varsta, data_angajare):
        super().__init__(nume, prenume, varsta)
        self.data_angajare = data_angajare


    def verifica_disponibilitate(self, carte):
        if isinstance(carte, CarteFizica):
            if carte.imprumutata:
                print("Cartea {} nu este disponibila!".format(carte.titlu))
                return False
            else:
                print("Cartea {} este disponibila!".format(carte.titlu))
                return True
