from countries import countries
import random

finalisti_uzorak = random.sample(countries, 26)
finalisti = []

for drzava, izvodjac, pjesma in finalisti_uzorak:
    el = {
        "drzava": drzava,
        "izvodjac": izvodjac,
        "pjesma": pjesma
    }
    finalisti.append(el)


bodovi = [12, 10, 8, 7, 6, 5, 4, 3, 2, 1]
for drzava, izvodjac, pjesma in countries:
    bez_drzave = []
    for item in finalisti:
        if item["drzava"] != drzava:
            bez_drzave.append(item)
    za_bodovanje = random.sample(bez_drzave, 10)
    brojac = 0
    for bod in bodovi:
        naziv_drzave = za_bodovanje[brojac]["drzava"]
        for finalist in finalisti:
            if finalist["drzava"] == naziv_drzave:
                finalist["bodovi"] = finalist.get("bodovi", 0) + bod
                break
        brojac += 1

finalisti = sorted(finalisti, key=lambda x: x['bodovi'], reverse=True)

bodovi = 0
for item in finalisti:
    bodovi += item["bodovi"]

print('Pobjednik: ',finalist,'Ukupni bodovi:',bodovi)


import re
reg = "$.{10}";

for item in finalisti:
	if re.search(reg, item['pjesma']):
		print(item)
print('Države koje u naslovu pjesme imaju vise od 10 slova: ',item)
