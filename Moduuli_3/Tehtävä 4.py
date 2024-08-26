vuosi_luku = int(input("Anna vuosiluku [vvvv]: "))

if(vuosi_luku % 4 == 0 and vuosi_luku % 100 != 0 or vuosi_luku % 400 == 0):
    print("Vuosi on karkausvuosi!")
else:
    print("Vuosi EI ole karkausvuosi!")


