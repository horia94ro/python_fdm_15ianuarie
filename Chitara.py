from InstrumentMuzical import InstrumentMuzical

class Chitara(InstrumentMuzical):

    def __init__(self, material, acordaj):
        super().__init__(material)
        self.acordaj = acordaj

    