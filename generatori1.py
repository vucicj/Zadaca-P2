'''
Napraviti generator funkcije za ispis svih parnih i svih neparnih brojeva
manjih od prosljeđenog parametra.
'''


def parni(broj):
    for br in range(broj):
        if br%2==0:
            yield br

def neparni(broj):
    for br in range(broj):
        if br%2!=0:
            yield br

broj=int(input("Unesite broj: "))

print("Parni brojevi su: ", list(parni(broj)))
print("Neparni brojevisu: ", list(neparni(broj)))
