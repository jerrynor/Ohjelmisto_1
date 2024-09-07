import math


def laske_pizzan_hinta(halkaisija, hinta):
    pizzan_pinta_ala = math.pi * pow(halkaisija, 2)
    pizzan_hinta = pizzan_pinta_ala / hinta
    return pizzan_hinta

pizza1_halkaisija = float(input("Anna ensimmäisen pizzan halkaisija: "))
pizza1_hinta = float(input("Anna ensimmäisen pizzan hinta: "))

pizza2_halkaisija = float(input("Anna toisen pizzan halkaisija: "))
pizza2_hinta = float(input("Anna toisen pizzan hinta: "))

pizza1_yksikköhinta = laske_pizzan_hinta(pizza1_halkaisija, pizza1_hinta)
pizza2_yksikköhinta = laske_pizzan_hinta(pizza2_halkaisija, pizza2_hinta)

if pizza1_yksikköhinta < pizza2_yksikköhinta:
    print("Ensimmäinen pizza antaa paremman vastineen rahallesi.")
elif pizza1_yksikköhinta > pizza2_yksikköhinta:
    print("Toinen pizza antaa paremman vasineen rahallesi.")
else:
    print("Pizzat antavat yhtä hyvän vastineen rahallesi.")





