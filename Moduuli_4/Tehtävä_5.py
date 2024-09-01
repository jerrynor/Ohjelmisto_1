käyttäjätunnus = ""
salasana = ""
syöttökerrat = 0
max_syöttökerrat = 5

while käyttäjätunnus != "python" and salasana != "rules" or käyttäjätunnus == "python" and salasana != "rules":
    käyttäjätunnus = input(("Anna käyttäjätunnus: "))
    salasana = input(("Anna salasana: "))
    if käyttäjätunnus != "python" and salasana != "rules":
        print("Käyttäjätunnus tai salasana on väärin. Yritä uudelleen.")
        syöttökerrat = syöttökerrat + 1
        if syöttökerrat > 5:
            print("Pääsy evätty")
            break
        else:
            print(f"Sinulla on {max_syöttökerrat - syöttökerrat} yritys jäljellä, ennen tilin lukkiutumista")
    elif käyttäjätunnus == "python" and salasana != "rules":
        print("Syöttämäsi salasana on väärin. Oletko unohtanut salasanasi? Yritä uudelleen.")
        syöttökerrat = syöttökerrat + 1
        if syöttökerrat > 5:
            print("Pääsy evätty")
            break
        else:
            print(f"Sinulla on {max_syöttökerrat - syöttökerrat} yritys jäljellä, ennen tilin lukkiutumista")
    else:
        print("Tervetuloa!")
