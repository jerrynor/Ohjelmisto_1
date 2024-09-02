import random

heittokerrat = 0
noppien_määrä = int(input("Anna heitettävien noppien määrä: "))
noppien_summa = 0

while heittokerrat < noppien_määrä:
    for i in range(noppien_määrä):
        nopan_arvo = random.randint(1, 6)
        noppien_summa = noppien_summa + nopan_arvo
        print(f"Heitit nopan luvun: {nopan_arvo}")
        heittokerrat += 1

print(f"Heitettyjen noppien summa on: {noppien_summa}")











