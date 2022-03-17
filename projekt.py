import random
pulka1 = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14]
pulka2 = []
random.shuffle(pulka1)
for i in range(26):
    cislo = random.choice(pulka1)
    pulka2.append(cislo)
    pulka1.remove(cislo)



while (len(pulka1) != 0 or len(pulka2) != 0):
    tri1 = []
    tri2 = []

    tri1 = pulka1[:3]
    tri2 = pulka2[:3]

    pulka1 = pulka1[3:]
    pulka2 = pulka2[3:]

    nejvyssicislo1 = max(tri1)
    nejvyssicislo2 = max(tri2)

    print(nejvyssicislo1)
    print(nejvyssicislo2)
    pocitac = random.randrange(9, 12)
    print(pocitac)
    
    print(tri1)
    print(tri2)
    x = input("chces vsadit karty? Y/N: ")
    if x == "Y" or nejvyssicislo2 > pocitac:
        print("sazka")
        
    
