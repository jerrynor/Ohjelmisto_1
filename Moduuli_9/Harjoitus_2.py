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


auto = Auto("ABC-123", 142)

print(f"{auto.rekisteritunnus} {auto.huippunopeus} km/h {auto.tamanhetkinen_nopeus} km/h {auto.kuljettu_matka}")

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

print(f"Kiihdytit auton nopeuteen: {auto.tamanhetkinen_nopeus} km/h")

auto.kiihdyta(-200)

print(f"Näit peuran tiellä ja teit hätäjarrutuksen! Nopeutesi on nyt {auto.tamanhetkinen_nopeus} km/h")




