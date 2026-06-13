def pgcd_division (a, b):
    etape = 0
    while b != 0 :
        a, b = b, a % b
        etape += 1
    return a, etape

def pgcd_soustraction (a, b):
    etape = 0
    while a != b :
        if a > b :
            a = a - b
        else :
            b = b - a
        etape += 1
    return a, etape

print()
a, b = int(input("Entrez a : ")), int(input("Entrez b : "))
#pgcd, nb_etape = pgcd_soustraction(a, b)
pgcd, nb_etape = pgcd_division(a, b)

print(f"\nLe PGCD obtenu est = {pgcd} en {nb_etape} étape(s)")

ppcm = (a * b) // pgcd
print(f"\nLe PPCM obtenu est = {ppcm}")