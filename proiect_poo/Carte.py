class Carte(object):

    def __init__(self, titlu, autor):
        self.titlu = titlu
        self.autor = autor


    def __repr__(self):
        return f"{self.titlu}, {self.autor}"