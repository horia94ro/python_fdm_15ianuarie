import math

class Punct:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f"Am creat un punct cu coordonatele: (X: {self.x}, Y: {self.y}) ")





    def calculeaza_distanta(self, punct2):
        dist = math.sqrt((self.x - punct2.x) ** 2 + (self.y - punct2.y) ** 2)
        return dist

# p1 = Punct(0,0)
# p2 = Punct(1,1)
# print(p1.calculeaza_distanta(p2))

class Triunghi:

    def __init__(self, baza, inaltime):
        self.baza = baza
        self.inaltime = inaltime

    def calculeaza_arie(self):
        return self.baza * self.inaltime / 2


t1 = Triunghi(10, 2)
print(t1.calculeaza_arie())


















