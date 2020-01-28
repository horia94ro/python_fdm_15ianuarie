from Pian import Pian
from Vioara import Vioara
from Chitara import Chitara

p1 = Pian("marmura", 120)
v1 = Vioara("cires", 5)
c1 = Chitara("nuc", True)

print(p1)
print(id(p1))
# for instanta in [p1, v1, c1]:
#     instanta.curata_instrument()

# for instanta in [p1, v1, c1]:
#     instanta.scoate_sunet() #arunca exceptie pentru metoda nu e implementata de Chitara
