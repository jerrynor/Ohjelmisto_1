class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinen_nopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = tamanhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

auto = Auto("ABC-123", "142 km/h", 0, 0)

print(f"{auto.rekisteritunnus} {auto.huippunopeus} {auto.tamanhetkinen_nopeus} {auto.kuljettu_matka}")