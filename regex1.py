'''
Potrebno napisati regex koji vraca podudaranje ukoliko se unese string koji počinje kao prvo slovo vašeg imena,
a završava kao prvo slovo prezimena. String mora sadržavati bar jedan broj između 0 i 5 i razmak.
'''

import re

string=input("Unesite string: ")
reg=r'^J.*\s[0-5].*V$'

if re.match(reg, string):
    print("Podudaranje pronađeno")
else:
    print("Nema podudaranja")
