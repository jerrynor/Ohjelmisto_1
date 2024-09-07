def parittomat_luvut(lista):
    parittomat_luvut = []
    for luku in lista:
        if luku % 2 == 0:
            parittomat_luvut.append(luku)
    return parittomat_luvut

kaikki_luvut = [1,2,3,4,5,6,7,8,9,10]

parilliset_luvut = parittomat_luvut(kaikki_luvut)

print(kaikki_luvut)
print(parilliset_luvut)