# import requests
#
# print(requests.__cake__)

class Pisica:
    """
    Clasa folosita pentru descrierea unei pisici
    """

    def __init__(self, culoare_blana = None, varsta = None, nume = None):
        self.culoare_blana = culoare_blana
        self.varsta = varsta
        self.nume = nume


    def spune_miau(self):
        self.matasoasa = True #atribut initializat inafara __init__-ului
        print("Meow! Numele meu este: {}".format(self.nume))

p1 = Pisica("gri", 3, "Leia")
p2 = Pisica("neagra", 2, "Sheba")
p3 = p2
print(p1.culoare_blana)
print(p2.nume)
p3.nume = "Tom"
print(p2.nume)
print(p1.matasoasa) #va genera exceptie pentru ca matasoasa nu a fost inca initializat
p1.spune_miau()
print(p1.matasoasa)
p2.spune_miau()
p4 = Pisica()
print(p4)