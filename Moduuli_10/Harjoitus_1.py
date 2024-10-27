import random

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = random.randint(alin_kerros, ylin_kerros)

    def siirry_kerrokseen(self, valittu_kerros):

        if valittu_kerros > self.ylin_kerros or valittu_kerros < self.alin_kerros:
            print(f"Kerrosta {valittu_kerros} ei ole olemassa ")
            return

        if self.nykyinen_kerros < valittu_kerros:
            while self.nykyinen_kerros < valittu_kerros:
                self.kerros_ylos()
        elif self.nykyinen_kerros > valittu_kerros:
            while self.nykyinen_kerros > valittu_kerros:
                self.kerros_alas()

    def kerros_ylos(self):

        if self.ylin_kerros == self.nykyinen_kerros:
            print("Olet ylimmässä kerroksessa.")
            return

        self.nykyinen_kerros = self.nykyinen_kerros + 1
        print(f"Nykyinen kerros: {self.nykyinen_kerros}")

    def kerros_alas(self):

        if self.alin_kerros == self.nykyinen_kerros:
            print("Olet alimmassa kerroksessa.")
            return

        self.nykyinen_kerros = self.nykyinen_kerros - 1
        print(f"Nykyinen kerros: {self.nykyinen_kerros}")



hissi = Hissi(1, 9)

hissi.siirry_kerrokseen(1)
