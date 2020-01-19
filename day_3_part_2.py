# def functie_1():
#     print("aceasta este o metoda fara parametrii")
#
# def functie_2(x):
#     return x ** 2
#
#
#
#
# def par_impar(x):
#     if x % 2 == 0:
#         print('valoare para')
#         return
#     print('valoare impara')
#
# functie_1()
# print(functie_2(9))
# # par_impar('sir de caractere') # Genereaza TypeError la rulare
# par_impar(10)

# def functie_suma(x, y = 10):
#     return x + y
#
# print(functie_suma(76))
# print(functie_suma(x = 34))
# print(functie_suma(x = 23, y = 74))
# print(functie_suma(78, 21))
# print(functie_suma(y = 15, x = 20))

def banner_message_of_the_day(mesaj, banner = '-'):
    lungime = len(mesaj)
    print(lungime * banner)
    print(mesaj)
    print(lungime * banner)
#
# banner_message_of_the_day("BINE ATI VENIT LA PYTHON")
# banner_message_of_the_day("SALUT", "*")\

def hypervolume(*args):
    for i in args:
        print(i, end = " ")
    print("Tipul de date al varargs este: {}".format(type(args)))
    # print(a)

def hypervolume_2(lista):
    for val in lista:
        print(val, end = " ")

# hypervolume()
# hypervolume(1, 2, 3)
# hypervolume(10)
# hypervolume(10, 20, 30, 40, 50)
# hypervolume_2([1, 2, 3, 4, 6])

def functie_key_word_args(item, **kwargs):
    print(item)
    print(kwargs)
    print(kwargs.values())
    print(kwargs.keys())

def exemplu_var_args(arg1, arg2, *args, cheie1, cheie2):
    print(arg1)
    print(arg2)
    print(args)
    print(cheie1)
    print(cheie2)

# exemplu_var_args(1, 2, 3, 4, cheie1 = 5, cheie2= 6)
# functie_key_word_args(item = 10)
# functie_key_word_args(10, cheie_1 = 20, cheie_2 = 30, cheie_3 = 40)


def minim_lista(lista):
    minim = lista[0]
    for i in lista[1:]:
        if i < minim:
            minim = i
    return minim


# print(minim_lista([0, 1, -1, -5, 100, -7, 3]))

def suma_lista(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

# print(suma_lista(1,2,3,4,5,6,7,8,9,10))

dict_tva_produse ={'alimentar':9, 'electrocasnic':7, 'imobiliar':19}
a = 10

def calcul_pret_final(pret_initial, tip_produs):
    pret_initial += pret_initial * 0.05
    if tip_produs in dict_tva_produse:
        pret_final = pret_initial + pret_initial * dict_tva_produse[tip_produs] / 100
    else:
        pret_final = pret_initial + pret_initial * 0.1
    return round(pret_final, 2)


# print(calcul_pret_final(100, 'imobiliar'))
# print(calcul_pret_final(37, 'alimentar'))
