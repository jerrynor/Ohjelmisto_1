"""
class Koira:
    pass

koira = Koira()

koira.name = "Tempo"
koira.age = 11
koira.rotu = "puudeli"

print(f"{koira.name} on pieni {koira.rotu}, joka on {koira.age} vuotta vanha.")
"""

class Koira:
    def __init__(self, name, age, race):
        self.name = name
        self.age = age
        self.race = race

koira = Koira("Tempo", 11, "puudeli")

print(f"{koira.name} on pieni {koira.race}, joka on {koira.age} vuotta vanha.")
