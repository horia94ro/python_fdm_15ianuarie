from InstrumentMuzical import InstrumentMuzical

class Pian(InstrumentMuzical):

    def __init__(self, material, nr_clape):
        super().__init__(material)
        self.nr_clape = nr_clape

    def __repr__(self):
        return "Pianul are {0} clape si este facut din {1}"\
                .format(self.nr_clape, self.material)

    def scoate_sunet(self):
        print("Sunet specific de pian")