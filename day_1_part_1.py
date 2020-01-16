print("HELLO WORLD")
s1 = "TELECOM" " ACADEMY"
s2 = "CURSUL DE " + "PYTHON"
print(s1)
print(s2)
s3 = "METRO SYSTEMS"
s4 = s3.lower()
print(s4)
print(s4.upper()) #s4 ramane nemodificat; se face in memorie un nou string pentru upper()

s5 = "hello world"
print(s5.capitalize())
print(s5.__len__())
print(len(s5))
print(s5.replace('hello', 'good bye'))
print(s5.replace('l', 'W', 2))
print(s5.find('l')) #prima aparitie in cadrul string-ului
print(s5.find("world"))  #prima pozitie de la care incepe sub-string-ul
print(s5.find('X')) # -1 reprezinta faptul ca valoarea cautata nu exista in string

s6 = "METRO SYSTEMS INVATA CCNA"
print(s6.replace("ccna".upper(), "python".upper()))
print(s6.lower().replace('ccna', 'python').upper())
sep = "-"
seq = ("UN", 'sir', 'separat', 'de', 'minus')

print(sep.join(seq))

s7 = "TELECOM"
s8 = "ACADEMY"
s9 = "CURSURI"
s10 = "PYTHON"
print(s7 + "+" + s8 + "+" + s9 + "+" + s10, end = " ")
print(s7, s8, s9, s10, sep="+")

s11 = "ANA ARE " + str(3 + 4) + " MERE"
print(s11)