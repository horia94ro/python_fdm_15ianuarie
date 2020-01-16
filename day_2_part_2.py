nume_utilizator = input("Introduceti userul: ")
print(len(nume_utilizator))
nume_utilizator = nume_utilizator.strip(str(9))
print(len(nume_utilizator))

sir = input("Introduceti sirul: ")
if len(sir) > 1:
    # rez = sir[:2] + sir[len(sir) - 2 : len(sir)]
    rez = sir[:2] + sir[-2:]
    print(rez)
else:
    print("Lungime prea mica a sirului!")

sir = input("Introduceti sirul: ")
for i in range(0, len(sir), 2):
    print(sir[i], end = " ")

print("")
for i in range(0, len(sir)):
    if i % 2 == 0:
        print(sir[i], end = " ")

lista = [1, 2, True]

lista_mea = [10, 20, "sir", True, 'telecom', 'python']
lista_mea.append("valoare noua") #adaugare in lista

lista_mea.append(10) #listele memoreaza/suporta elementele duplicate
# lista_mea.sort() #va genera exceptie pentru ca am tipuri diferite de date
lista_mea.reverse()
print(lista_mea[1:5]) #slicing-ul merge identic ca la string-uri
print(lista_mea[3])
# print(lista_mea[99]) #va genera IndexError - nu exista indexul in cadrul listei mele
print(lista_mea.index('sir')) #prima aparitie a elementului cautat

lista_mea.remove("telecom") #metoda nu returneaza nimic; exceptie daca nu elementul nu exista

del lista_mea[3] #statement, diferit de apelul metodei remove de mai sus

print(lista_mea.pop()) #cand pop() nu are argument, returneaza si elimina ultimul element

print(lista_mea.pop(0)) #elimina elementul de pe pozitia 0 si il returneaza


nr = int(input("Cate valori doriti introduse?"))
lista_val = []
for i in range(0, nr):
    lista_val.append(int(input("Valoarea cu indexul {0}: ".format(i))))

print("Lista initiala este: ", lista_val)
for i in range(0, nr):
    lista_val[i] = lista_val[i] ** 2

print("Lista finala este: ", lista_val)

rez = [i ** 2 for i in lista_mea]

lista_2 = ['rosu', 'verde', 'albastru', 'galben']


rez = [var.upper() for var in lista_2]
print(rez)
rez = [var for var in lista_2 if len(var) == 4]
print(rez)

# Cititi de la tastatura N elemente intr-o lista; intr-o lista secundara
# pastrati doar valorile unice

N = int(input("Cate valori adaugam in lista?"))
lista_init =[]
for i in range(0, N):
    lista_init.append(int(input("Valoarea {}: ".format(i))))

lista_unice = []
for i in lista_init:
    if i not in lista_unice:
        lista_unice.append(i)
    else:
        pass

print(lista_unice)

setul_meu = {10, 20, "sir", True, 10, 20, False, "sir"}
setul_meu.add(47)
setul_meu.add(47)
setul_meu.add(50)
setul_meu.add("sir")
print(setul_meu)
setul_meu.update([10, 11, 12, 13, 14, 15])
print(setul_meu)
# print(setul_meu[4]) #set-urile NU se indexeaza asemanator tuplurilor/listelor
setul_meu.remove(20)
# setul_meu.remove(20) #KeyError daca incerc sa elimin ceva ce nu exista
print(setul_meu)
setul_meu.discard(20) #NU va mai arunca eroare la momentul rularii, chiar daca elementul nu exista



# dictionar = {'cheie_1':10, 'cheie_2':30, 'cheie_3':45, 'cheie_4':True}
# print(dictionar['cheie_1'])
# dictionar['cheie_2'] = 44
# print(dictionar)
persoana = {'nume':'', 'varsta': '', 'e-mail':"horia.calin@telacad.ro"}
persoana.update({'nume':'Horia', 'varsta':25})
# print(persoana)
# persoana['culoare_ochi'] = 'caprui'
# print(persoana)


# persoane_varsta = [ ('Tudor', 17), ('Laur', 29), ('Daniela', 27), ('Tudor', 28)]
# dict_pers_varsta = dict(persoane_varsta)
# print(dict_pers_varsta)

print(list(persoana.keys()))
print(list(persoana.values()))
print(persoana.items())

for k, v in persoana.items():
    print("Cheia este: {0}, valoarea: {1}".format(k, v))











