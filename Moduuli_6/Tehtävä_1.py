def arvo_noppa():
    import random
    arvo_nopanluku = random.randint(1,6)
    return arvo_nopanluku

noppa = arvo_noppa()
heitot = 0

while noppa != 6:
    noppa = arvo_noppa()
    heitot = heitot + 1
    print(f"Nopanluku: {noppa}")

print(f"Heitit noppaa {heitot} kertaa.")


