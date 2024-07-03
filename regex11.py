'''
Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
Nakon toga napisati regex za provjeru eduId koji mora biti formata iprezimeX@sum.ba gdje je i prvo slovo imena + prezime.
X predstavlja bilo koji broj (moze ici u beskonacnost), a taj broj ne mora postojati (može biti samo iprezime@sum.ba).
Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.
'''

import re

email = input("Unesite e-mail (ime.prezime@fpmoz.sum.ba): ")
eduid = input("Unesite eduId (iprezimeX@sum.ba): ")

regex = r'^[a-z]+\.[a-z]+@fpmoz\.sum\.ba$'
reg = r'^[a-z][a-z]+[0-9]*@sum\.ba$'


if re.match(regex, email):
    print("E-mail je validan.")
else:
    print("E-mail nije validan.")

if re.match(reg, eduid):
    print("EduId je validan.")
else:
    print("EduId nije validan.")
    
