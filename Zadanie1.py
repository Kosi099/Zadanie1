# liczba = 0
# liczba = "0"
# liczba = 0.0



# def funkcja():
#     print(liczba+liczba)
#     print("Ala")
#     print(liczba)

print("Ala ma " + " 5 lat") # konkatencja
print(0 - 1)
print(2 / 1)
print(2 * 1)
print(2 // 1) # dzielenie bez reszty
print(2 % 1) # modulo
print(2 ** 1) # potegowanie
print(5)
print("Ala ma 5 lat")
# print("Ala ma " + 5 + " lat") błąd
lata = 5
print("Ala ma " + str(5) + " lat")

print("Ala ma {} lat".format(5))

print("Ala ma {1} lat a Marta {0}".format(5,10))

# f-string (od python 3.6)
print(f"Ala ma {5} lat")

imie = "Małgorzata"
print(imie[4])

imie = imie.lower()
print(imie)

"Wojtek".lower().lstrip().rsplit()

# listy

lista = []
print(type(lista))
lista.append(5)
lista.insert(0, 6)
lista2 = [1, 2, 3, 4, 5, 6]
lista2[3]
lista3 = lista + lista2
print(lista3)

lista4 = [1, "Ala", imie, 3.4, [1,3]]
print(lista4[4][1])

macierz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(macierz)
print("Srodkowe miejsce = " + str(macierz[1][1]))

# slownik

slownik = {}
print(type(slownik))
slownik["imie"] = "Marek"
print(slownik)
slownik2= {
    'imie': 'Marek',
    'Wiek': 25,
    'Wzrost' : 180}
print(slownik2)
print(slownik2.keys())
print(slownik2.items())
print(slownik2['Wiek'])

def pow():
    pass



# Importy

# from math import *
# from math import pow

import math as m

m.pow(2, 2)