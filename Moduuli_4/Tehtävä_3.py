
suurin_luku = None
pienin_luku = None

while True:
    syöte = input("Syötä luku: ")

    if syöte == "":
        break

    syötetty_luku = int(syöte)

    if suurin_luku is None and pienin_luku is None:
        suurin_luku = syötetty_luku
        pienin_luku = syötetty_luku
    else:
        if syötetty_luku > suurin_luku:
            suurin_luku = syötetty_luku
        if syötetty_luku < pienin_luku:
            pienin_luku = syötetty_luku

if suurin_luku is not None and pienin_luku is not None:
    print(f"Suurin luku: {suurin_luku}")
    print(f"Pienin luku: {pienin_luku}")












