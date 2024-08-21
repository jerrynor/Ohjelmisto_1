#Muuttujat ja vuorovaikutteiset ohjelmat

"""
#1.
print("Mikä sinun nimesi on?")
nimi = input()
print("Hei " + nimi + "!")

#2
print("Anna ympyrän säde:")
ympyranSade = float(input())
pii = 3.141
ympyranPintaAla = ympyranSade * ympyranSade * pii
print(ympyranPintaAla)

#3
kanta = float(input("Anna suorakulmion kannan, pituus: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

suoraKulmionPiiri = kanta + korkeus * 2
suoraKulmionPintaAla = kanta * korkeus
print("Suorakulmion piiri on: " + str(suoraKulmionPiiri))
print("Suorakulmion pinta-ala on: " + str(suoraKulmionPintaAla) +" m2")


#4
luku1 = int(input("Anna ensimmäinen kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))
luku3 = int(input("Anna kolmas kokonaisluku: "))

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3

print(summa)
print(tulo)
print(keskiarvo)


#5
import math

gramma = 1
kilogramma = gramma * 1000

luoti = gramma * 13.3
naula = luoti * 32
leiviskä = naula * 20

leiviskäMäärä = float(input("Anna leiviskämäärä: ")) * leiviskä
naulaMäärä = float(input("Anna naulamäärä: ")) * naula
luotiMäärä = float(input("Anna luotimäärä: ")) * luoti

kokonaisMassaGrammoina = leiviskäMäärä + naulaMäärä + luotiMäärä
kokonaisMassaKiloina = kokonaisMassaGrammoina / kilogramma

pyöristettyMassa = math.floor(kokonaisMassaKiloina)
yliJääneetGrammat = kokonaisMassaKiloina - pyöristettyMassa

print(f"Massa nykymittojen mukaan:\n{pyöristettyMassa} kilogrammaa ja {yliJääneetGrammat * kilogramma:.2f} grammaa")
"""

#6
import random

lukonNumero = 0

print("Kolminumeroisen lukon koodi on: ")
for i in range(3):
    lukonNumero = random.randrange(0, 9)
    print(lukonNumero)

print("Nelinumeroisen lukon koodi on:")
for i in range(4):
    lukonNumero = random.randrange(1, 6)
    print(lukonNumero)













