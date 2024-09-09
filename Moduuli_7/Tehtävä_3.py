lentoasemat = {}

while True:
    syötä_lentoaseman_tiedot = input("Haluatko syöttää uuden lentoaseman? (K/E): ").upper()

    if syötä_lentoaseman_tiedot == "K":
        lentoaseman_nimi = input("Syötä lentoaseman nimi: ")
        lentoaseman_ICAO_koodi = input("Syötä lentoaseman ICAO koodi: ").upper()
        lentoasemat[lentoaseman_ICAO_koodi] = lentoaseman_nimi

    elif syötä_lentoaseman_tiedot == "E":
        hae_lentoaseman_tiedot = input("Haluatko hakea lentoaseman tietoja? (K/E): ").upper()

        if hae_lentoaseman_tiedot == "K":
            lentoaseman_ICAO_koodi = input("Anna lentoaseman ICAO koodi: ").upper()

            if lentoaseman_ICAO_koodi in lentoasemat:
                print(f"Lentoasema: {lentoasemat[lentoaseman_ICAO_koodi]}")
            else:
                print("Lentoasemaa ei löytynyt annetulla ICAO-koodilla.")
        else:
            print("Ohjelma sulkeutuu.")
            break

    else:
        lopeta = input("Haluatko lopettaa? K/E: ").upper()
        if lopeta == "K":
            print("Ohjelma sulkeutuu.")
            break









