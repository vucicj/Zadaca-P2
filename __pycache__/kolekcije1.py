'''Potrebno je kreirati evidenciju odrađenih sati i isplata radnika tvrtke koja se bavi dostavljanjem.
Generirati 15 radnika random imena i prezimena iz ponuđene liste, te njegovu satnicu slučajnim odabirom floata između 4 i 6 zaokruženu na 2 decimale.
Sve radnike spremiti u listu radnika, a jedan radnik je rječnik oblika 
{“ime”: “John”, “prezime”: “Doe”, “satnica”: 5.20}
Iterirati kroz sve radnike i dodati im novo svojstvo “tjedni_sati” koji generira cijeli broj odrađenih sati u 1 tjednu od 20 do 30.
Nakon toga napraviti obračun množenjem satnice sa tjednim satima i rezultate spremiti u listu tuple-a (trojki) oblika (ime, prezime, isplata).
Iteriranjem ispisati podatke, a zatim izračunati ukupnu i prosječnu isplatu za taj tjedan.
Ispisati Imena svih radnika koji imaju isplatu iznad prosječne.'''


imena=['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John',
'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan',
'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']
prezimena=['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez',
'Cleary', 'Hoyman', 'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 'Cornett', 'Smith',
'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']
import random
radnici=[]
for _ in range(15):
    imena1=random.choice(imena)
    prezimena1=random.choice(prezimena)
    satnica=round(random.uniform(4, 6), 2)
    radnici.append({"ime": imena1, "prezime": prezimena1, "satnica": satnica})

for radnik in radnici:
    radnik["tjedni_sati"]=random.randint(20 ,30)

print(radnici)



tuple_radnika=[]
ukupna_isplata=0
for radnik in radnici:
    ime=radnik["ime"]
    prezime=radnik["prezime"]
    satnica=radnik["satnica"]
    tjedni_sati=radnik["tjedni_sati"]              
    tjedna_isplata=round(satnica*tjedni_sati, 2)
    tuple_radnika.append((ime, prezime, tjedna_isplata))
    ukupna_isplata+=tjedna_isplata

print("Isplate: " )
for ime, prezime, isplata in tuple_radnika:
    print(f"{ime} {prezime}: {isplata}")
print("-----------------------------------------------------------------")
prosjecna_isplata=ukupna_isplata/len(radnici)
print(f"Ukupna tjedna isplata: {ukupna_isplata}")
print(f"Prosjecna tjedna isplata: {prosjecna_isplata}")
print("-----------------------------------------------------------------")
print("Radnici s isplatom iznad prosjeka:")
for ime, prezime, isplata in tuple_radnika:
    if isplata > prosjecna_isplata:
        print(f"{ime} {prezime}")

