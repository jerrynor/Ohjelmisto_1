
kokonaisluku = int(input("Anna kokonaisluku: "))

on_alkuluku = True

if kokonaisluku < 2:
    on_alkuluku = False
else:
    for i in range(2, kokonaisluku):
        if kokonaisluku % i == 0:
            on_alkuluku = False
            break
if on_alkuluku:
    print(f"Luku {kokonaisluku} on alkuluku.")
else:
    print(f"Luku {kokonaisluku} ei ole alkuluku.")



