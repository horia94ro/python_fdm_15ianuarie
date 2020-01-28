from proiect_poo.Carte import Carte

class CarteFizica(Carte):

    def __init__(self, titlu, autor, locatie, editura, imprumutata = False):
        super().__init__(titlu, autor)
        self.locatie = locatie
        self.editura = editura
        self.imprumutata = imprumutata