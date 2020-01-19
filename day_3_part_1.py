# lista = []
#
# while True:
#     var = input("Introduceti textul... ")
#     if var != '':
#         lista.append(var)
#     else:
#         break
#
# max = -1
# for item in lista:
#     if len(item) > max:
#         max = len(item)
#         elem = item
# print(f"Cel mai lung sir este: {elem} cu lungime {max}")


# mesaj = input("Introduceti tot textul pe o singura linie... ").strip()
# lista = mesaj.split(" ")
# dictionar_aparitii = {}
# for cuvant in lista:
#     if cuvant in dictionar_aparitii:
#         dictionar_aparitii[cuvant] += 1
#
#
#     else:
#         dictionar_aparitii[cuvant] = 1
#         # dictionar_aparitii.update({cuvant : 1})
#
# for k, v in dictionar_aparitii.items():
#     print(f"Cuvantul \"{k}\" se repeta de {v} ori")


numar_secunde = 187524
#
# sec_min = 60
# sec_ora = 60 * sec_min
# sec_zi =  24 * sec_ora
#
# rez = ()
# t = (sec_zi, sec_ora, sec_min)
# for i in t:
#     var = int(numar_secunde//i)
#     rez += (var, )
#     numar_secunde = numar_secunde - var * i
#
# print(rez)

# dictionar = {'sec':60, 'min':60, 'ore':24, 'zile':365}
# rez = ()
# for div in dictionar:
#     rez +=  (numar_secunde % dictionar[div], )
#     numar_secunde = numar_secunde // dictionar[div]
#
# rez +=  (numar_secunde, )
# print(rez)







