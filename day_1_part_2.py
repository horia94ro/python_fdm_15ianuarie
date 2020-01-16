# nume = input("Cum te numesti?")
# print("Salut, " + nume)
# print("Introduceti numerele")
# a = int(input("a: "))
# b = int(input("b: "))
# suma = a + b
# print("Suma este: %s" % (suma))
# ---------------------------------EXERCITII
# sir = input("Introduceti textul: ")
# sir += " Telecom preda cursul de Python "
# sir += str(3)
# sir += " dar face analogie cu Python 2"
# print(sir)

# import getpass
# username = input("Username: ")
# parola = getpass.getpass("Parola: ")
# print(parola)

sir = "Telecom Academy preda o multime de cursuri"
sir = sir.replace("preda", "ofera")
print(sir)

rest = 5 % 2
print("Restul impartirii este: ", rest)

x = 'blue, red, green'
print(x.split(", "))