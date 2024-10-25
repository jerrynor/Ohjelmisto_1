import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        self.tamanhetkinen_nopeus += nopeuden_muutos
        if self.tamanhetkinen_nopeus < 0:
            self.tamanhetkinen_nopeus = 0
        elif self.tamanhetkinen_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus

    def kulje(self, tunnit):
        self.kuljettu_matka += self.tamanhetkinen_nopeus * tunnit

autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

kilpailu_kaynnissa = True

while kilpailu_kaynnissa:
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)

        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False
            break

print(f"{'Rekisteritunnus':<20}{'Huippunopeus (km/h)':<20}{'Nopeus (km/h)':<20}{'Kuljettu matka (km)':<20}")
for auto in autot:
    print(f"{auto.rekisteritunnus:<20}{auto.huippunopeus:<20}{auto.tamanhetkinen_nopeus:<20}{auto.kuljettu_matka:<20.2f}")
