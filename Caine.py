import os
class Caine:

    rasa = "Labrador" #membru static al clasei
    def __init__(self, nume, varsta, culoare):
        self._nume = nume
        self._varsta = varsta
        self._culoare = culoare

    def afiseaza_nume(self):
        print(self._nume)

    def modifica_nume(self, noul_nume):
        self._nume = noul_nume

    @staticmethod
    def latra():
        # self.culoare = "alb"
        print("Woof!")


print(Caine.rasa)
c1 = Caine("Bolt", 1, "auriu")
c1.afiseaza_nume()
# c1.rasa = "Caine-lup"
print(c1.rasa) #ASA NU - zona de memorie este statica
print(Caine.rasa) #ASA DA
c1.latra() #ASA NU - metoda este statica
Caine.latra() #ASA DA
