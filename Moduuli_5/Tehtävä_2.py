
syöte = input("Anna luku: ")
luvut = []

while syöte != "":
    if syöte == "":
        break
    else:
        luvut.append(syöte)
        syöte = input("Anna luku: ")

luvut.sort(reverse=True)
print(luvut)