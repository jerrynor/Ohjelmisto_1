def gallonat_litroiksi(gallona):
    return gallona * 3.785

while True:
    muunna_gallonat = float(input("Syötä gallonat: "))

    if muunna_gallonat < 0:
        print("Syötit väärän arvon. Ohjelma sammuu.")
        break

    litra_määrä = gallonat_litroiksi(muunna_gallonat)

    print(f"{muunna_gallonat} gallonaa on {litra_määrä} litraa.")


