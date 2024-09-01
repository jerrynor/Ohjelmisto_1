import math
import random

N = int(input("Syötä pisteiden määrä: "))

n = 0
arvotut_pisteet = 0

while arvotut_pisteet < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if pow(x, 2) + pow(y, 2) < 1:
        n += 1
    arvotut_pisteet += 1

piin_likiarvo = 4 * n / N

print(piin_likiarvo)

