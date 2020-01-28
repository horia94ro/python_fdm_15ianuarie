from InstrumentMuzical import InstrumentMuzical

class Vioara(InstrumentMuzical):

    def __init__(self, material, nr_corzi):
        super().__init__(material)
        self.nr_corzi = nr_corzi

    def scoate_sunet(self):
        print("Sunet de vioara")