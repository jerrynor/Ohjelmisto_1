hytti_luokka = input("Mikä teidän hyttiluokkanne on? [LUX, A, B, C, D]: ")

if hytti_luokka == "LUX":
    print("parvekkeellinen hytti yläkannella")
elif hytti_luokka == "A":
    print("ikkunallinen hytti autokannen yläpuolella")
elif hytti_luokka == "B":
    print("ikkunaton hytti autokannen yläpuolella")
elif hytti_luokka == "C":
    print("ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka!")
