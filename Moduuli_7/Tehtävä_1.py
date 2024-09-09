vuoden_ajat = ("kevät", "kesä", "syksy", "talvi")

syötetty_kuukausi = int(input("Syötä kuukauden numero (1-12): "))

if 1 <= syötetty_kuukausi <= 12:
    if 3 <= syötetty_kuukausi <= 5:
        print(f"On siis {vuoden_ajat[0]}, kuljen Hakaniemen rantaan")
    elif 6 <= syötetty_kuukausi <= 8:
        print(f"On {vuoden_ajat[1]}")
    elif 9 <= syötetty_kuukausi <= 11:
        print(f"On {vuoden_ajat[2]}")
    else:
        print(f"On {vuoden_ajat[3]}")
else:
    print("Ei ole kuukauden numero, syötä luku väliltä 1-12.")



