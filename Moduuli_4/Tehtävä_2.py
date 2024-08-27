tuuma = 2.54

while tuuma > 0:
    senttimetri = float(input("Anna muunnettava tuumamäärä: "))
    if tuuma * senttimetri < 0:
        break
    print(f"{senttimetri} tuumaa on {tuuma * senttimetri} senttimetriä")

print("Ohjelman suoritus loppui.")


