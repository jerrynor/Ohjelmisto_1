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

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.hissit = []
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.luo_hissit(hissien_maara)

    def luo_hissit(self, maara):
        for i in range(maara):
            self.hissit.append(Hissi(self.alin_kerros, self.ylin_kerros))

    def aja_hissia(self, hissin_nro, tavoitekerros):
        ajettava_hissi = self.hissit[hissin_nro - 1]
        ajettava_hissi.siirry_kerrokseen(tavoitekerros)

    def palohalytys(self):
        print("Palohälytys!")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)


hissi = Hissi(1, 9)

talo = Talo(1, 9, 3)

talo.palohalytys()




