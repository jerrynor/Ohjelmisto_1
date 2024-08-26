kuhan_pituus = float(input("Kuinka pitkä kuha on?(cm): "))
ala_mittainen = 37

if kuhan_pituus < ala_mittainen:
    print(f"Kuha on {ala_mittainen - kuhan_pituus} cm liian pieni. Päästä se takaisin järveen")
else:
    print(f"Kuha on sopivan kokoinen!")