import random

arvottava_luku = random.randrange(1, 9)

arvaus = ""

while arvaus != arvottava_luku:
    arvaus = int(input("Arvaa luku väliltä 1-10: "))
    if arvaus > arvottava_luku:
        print("Numero on pienempi!")
    elif arvaus < arvottava_luku:
        print("Numero on suurempi!")
    else:
        print("Arvasit oikein!")
        break