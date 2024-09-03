def arvo_noppa(tahko):
    import random
    arvo_nopanluku = random.randint(1,tahko)
    nopanluku = arvo_nopanluku
    return nopanluku

nopan_maxluku = int(input("Moni tahkoista noppaa haluat heittää?: "))
noppa = arvo_noppa(nopan_maxluku)
heitot = 0

while noppa != nopan_maxluku:
    noppa = arvo_noppa(nopan_maxluku)
    heitot = heitot + 1
    print(f"Nopanluku: {noppa}")

print(f"Heitit noppaa {heitot} kertaa.")


