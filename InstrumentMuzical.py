class InstrumentMuzical:

    def __init__(self, material):
        self.material = material

    def scoate_sunet(self):
        raise NotImplementedError("Metoda abstracta nu este definita inca!")

    def curata_instrument(self):
        print("Se curata instrumentul")