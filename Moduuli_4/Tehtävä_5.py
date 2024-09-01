käyttäjätunnus = ""
salasana = ""
syöttökerrat = 0
max_syöttökerrat = 5

while käyttäjätunnus != "python" or salasana != "rules":
    käyttäjätunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    syöttökerrat += 1

    if käyttäjätunnus != "python" or salasana != "rules":
        if syöttökerrat >= max_syöttökerrat:
            print("Pääsy evätty")
            break
        else:
            print("Käyttäjätunnus tai salasana on väärin. Yritä uudelleen.")
            print(f"Sinulla on {max_syöttökerrat - syöttökerrat} yritys jäljellä, ennen tilin lukkiutumista")
    else:
        print("Tervetuloa!")
