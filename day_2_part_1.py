#Exercitiu 3 PPT Curs 2
# lista = ['telacad', 'peste 10 ani vechime', 'predare', 'cursuri online']
#
# text = input("Introduceti textul: ").lower()
#
# while text != "telacad":
#     text = input("Introduceti textul: ").lower()
#
#
# sir = ''
# for i in lista:
#     sir += i + " "
#
# for i in range(len(lista)):
#     sir += lista[i] + " "
# print(sir)
# sir = " ".join(lista)
# print(sir)
# print('telacad', 'peste 10 ani vechime', 'predare', 'cursuri online', sep = " ")

#Exercitiu 4 PPT Curs 2

# import math as mate
#
# x = 2 + 3j
#
# if isinstance(x, int):
#     print("x este integer")
#     print(x + 3)
# elif isinstance(x, float):
#     print("x este float")
#     print(x / 2)
# elif isinstance(x, complex):
#     print("x este imaginar")
#     # parte_reala = x.real
#     # parte_imag = x.imag
#     rez = mate.sqrt(x.real ** 2 + x.imag ** 2)
#     print(rez)
# else:
#     print("Tipul de date NU este numeric")

#Exercitiu 5

# val_max = int(input("Pana la ce valoare iteram? "))
# for i in range(1, val_max):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FIZZ BAR")
#     elif i % 3 == 0:
#         print("FIZZ")
#     elif i % 5 == 0:
#         print("BAR")
#     else:
#         print(i)


#Exercitiu optional 1 PPT Curs 2
# valoare = int(input("Valoare: "))
# if valoare % 2 == 0:
#     print("Valoarea este para")
# else:
#     print("Valoarea este impara")
#
# prim = True
# if valoare > 1:
#     for i in range(2, valoare // 2 + 1):
#         if valoare % i == 0:
#             prim = False
#             break
#
# if prim:
#     print("Valoarea prima")
# else:
#     print("Valoarea NU este prima!")

#Fibonacci
# n = 5
# a = 0
# b = 1
# print(a, b, end = " ", sep = " ")
# for i in range(1, n + 1):
#     c = a + b
#     a = b
#     b = c
#     print(c, end = " ")
#!!!!!
# sir = "telecom, 1;academy, 2;lala, 3"
# rez = (sir.split(";"))
# for i in range(len(rez)):
#     rez[i] = rez[i].split(",")
# print(rez)
