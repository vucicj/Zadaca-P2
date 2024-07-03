'''
Napisati rekurzivnu funkciju koja kao parametar prima string,
a kao rezultat taj string ispisuje sa zada.
'''

def obrnutistring(string):
    if len(string) == 0:
        return
    else:
        print(string[-1], end='')
        obrnutistring(string[:-1])

string1=input("Unesite string: ")
obrnutistring(string1)
