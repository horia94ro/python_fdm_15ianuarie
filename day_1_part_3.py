# a = 20
# b = 15
#
# if a < b:
#     print("a mai mic decat b")
# elif a == b:
#     print("a este egal cu b")
# elif a > b:
#     print("a mai mare decat b")
# else:
#     print("valorile nu pot fi comparate")
#
# if a < b:
#     print("a mai mic decat b")
# else:
#     if a == b:
#         print("a este egal cu b")
#     else:
#         if a > b:
#             print("a mai mare decat b")
#         else:
#             print("valorile nu pot fi comparate")


# if 1:
#     print("Aceasta expresie este mereu executata")


# a = input("Introduceti anotimpul: ").lower()
# if a == "vara":
#     print("CHALD")
# elif a == "iarna":
#     print("FREG")
# elif a == "toamna" or a == "primavara":
#     print("PLOO!")
# else:
#     print("Anotimpul introdus nu e corect")

# ora = int(input("ORA ESTE: [0;23]"))
# if ora >= 6 and ora < 12:
#     print("BUNA DIMINEATA")
# elif ora >= 12 and ora < 18:
#     print("BUUNA ziua")
# elif ora >= 18 and ora < 23:
#     print("buna seara")
# elif (ora >= 0) and ora < 24:
#     print("somn usor")
# else:
#     print("ora invalida")



# a = 10
# while a > 0:
#     a -= 1
#     if a % 2 == 0:
#         continue
#     print(a, end = " ")
#     if a == 5:
#         break

# for i in range(10):
#     print(i, end = " ")
#
# for i in range(2, 10, 2):
#     print(i, end = " ")

# cuvinte = ['telecom', 'academy', 'cursuri', 'python', 'java']
# for cuv in cuvinte:
#     print("Cuvantul {0} are lungimea: {1}".format(cuv, len(cuv)))
#
# for index in range(len(cuvinte)):
#     print(cuvinte[index], end = " ")


#-------------------EXERCITII
#
# text = input("Care este prescurtarea academiei?").lower()
# while text != "telacad":
#     print("TEXT INCORECT")
#     text = input("Care este prescurtarea academiei?").lower()
#
# print("SFARSIT PROGRAM")
#
# text = input("Care este prescurtarea academiei?").lower()
# while text != "telacad":
#     text = input("Care este prescurtarea academiei?").lower()
#     if text == "telacad":
#         break
#
#
# print("SFARSIT PROGRAM")

a = input("a: ")
while not a.isnumeric()or int(a) <= 2:
    a = input("reintroduceti a: ")
sum = 0
a = int(a)
for i in range(1, a + 1):
    sum += i

print(sum)


