class Animal(object): #mostenit in mod implicit
    def __init__(self, culoare, talie):
        self.culoare = culoare
        self.talie = talie

    def deplaseaza(self):
        return 10

    def doarme(self):
        print("Animalul doarme...")



class Urs(Animal):


    def __init__(self, culoare, talie, perioada_hibernare):
        super().__init__(culoare, talie)
        self.perioada_hibernare = perioada_hibernare

    def deplaseaza(self):
        return 7

class Pantera(Animal):

    def __init__(self, culoare, talie, coada):
        super().__init__(culoare, talie)
        self.coada = coada

    def deplaseaza(self, obosit = False):
        if obosit:
            return super().deplaseaza()
        else:
            return 45


smokey = Urs("brun", 100, 3)
p1 = Pantera("roz", 75, True)
a1 = Animal("alb", 50)
print(a1.deplaseaza())
# smokey.doarme()
# print(smokey.deplaseaza())
# print(smokey.culoare)
# print(smokey is Animal)
# print(isinstance(smokey, Animal))
# print(isinstance(p1, Urs))
# print(isinstance(p1, Animal))
# if isinstance(p1, Urs):
#     print(p1.perioada_hibernare)
# else:
#     print("Panterele nu hiberneaza")
print(smokey.deplaseaza())
print(p1.deplaseaza())
print(p1.deplaseaza(True))


