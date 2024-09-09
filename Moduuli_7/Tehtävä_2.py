
nimet = set()

while True:
    nimi = input("Syötä nimi: ")
    if nimi == "":
      break
    if nimi in nimet:
        print("Nimi on jo syötetty aiemmin")
    else:
        print("Tämä on uusi nimi")
        nimet.add(nimi)

for nimi in nimet:
    print(nimi)