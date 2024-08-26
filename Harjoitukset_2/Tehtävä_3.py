sukupuoli = input("Mikä on sukupuolesi? M/N: ")
hemoglobiini_arvo = float(input("Anna hemoglobiiniarvosi: "))

sukupuoli = sukupuoli.upper()

if(sukupuoli == "M" and hemoglobiini_arvo > 195):
    print("Hemoglobiiniarvosi on liian korkea!")
elif(sukupuoli == "M" and hemoglobiini_arvo < 134):
    print("Hemoglobiiniarvosi on liian matala!")
elif(sukupuoli == "N" and hemoglobiini_arvo > 175):
    print("Hemoglobiiniarvosi on liian korkea!")
elif(sukupuoli == "N" and hemoglobiini_arvo < 117):
    print("Hemoglobiiniarvosi on liian matala!")
else:
    print("Hemoglobiiniarvosi on normaali.")