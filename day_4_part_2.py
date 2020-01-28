# try:
#     x = 5
#     y = 1
#     print(x / y)
#     print("Instructiuni post impartire")
#     lista = [1, 2, 3]
#     lista[0] = 10
#     x = 5 + 6
# except ZeroDivisionError as e:
#     print("Ai incercat sa imparti la 0!")
#     print(str(e))
# except IndexError as e:
#     print("Te-ai referit la un index inexistent!")
# except TypeError as e:
#     print(str(e))
# except Exception as e:
#     print("Exceptia generala")
# else:
#     print("Instructiuni executate cand NU am exceptii (bloc else)")
# finally:
#     print("Instructiuni executate intotdeauna (bloc finally)")

# try:
#     x = 5
#     if x > 0:
#         e = ValueError("Valoarea lui x este mai mare decat 0!")
#         raise e
# except ValueError as e:
#     print(str(e))
#     print("Schimba valoarea lui x!")


# from day_4_part_1 import citeste_cuvinte
# print(citeste_cuvinte("my_file.txt"))
# import day_4_part_1
# # print("\n" + __name__)
# print(day_4_part_1.citeste_cuvinte("my_file.txt"))



#EXERCITIU PPT CAP 4 - SLIDE 30

def citeste_elemente(nr_elemente):
    lista_elemente = []
    for i in range(0, nr_elemente):
        val = input("Valoarea {}: ".format(i + 1))

        lista_elemente.append(val)
    return lista_elemente

def conversie_elem_lista(lista):
    lista_finala = []
    lista_except = []
    for item in lista:
        try:
            lista_finala.append(float(item))
        except ValueError as e:
            print(str(e))
            lista_except.append(item)
    return  lista_finala, lista_except

nr_valori = int(input("Cate valori vreau introduse in lista: "))
lista_init = citeste_elemente(nr_valori)
tuplu_liste = conversie_elem_lista(lista_init)
print("Elemente convertite: ", tuplu_liste[0])
print("Elemente neconverite: ", tuplu_liste[1])























