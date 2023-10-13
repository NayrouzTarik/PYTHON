import math 

while True:
    print("Liste des operations")
    print("--------------------")
    print("Somme            taper 1")
    print("Soustraction     taper 2")
    print("Multiplication   taper 3")
    print("Division         taper 4")
    print("Puissance        taper 5")
    print("Racine carre     taper 6")
    print("Carre            taper 7")
    print("Cube             taper 8")
    print("Valeur absolue   taper 9")
    print("PGCD             taper 10")
    print("Factorielle      taper 11")
    print("Quitter          taper 0")

    choix = int(input("Donnez votre choix = "))

    if choix == 0:
        print("Good bye")
        break

    elif choix == 1:
        a = float(input("Donner le premier nombre = "))
        b = float(input("Donner le deuxieme nombre = "))
        result = a + b
        print(f"La somme est = {result}")

    elif choix == 2:
        a = float(input("Donner le premier nombre = "))
        b = float(input("Donner le deuxieme nombre = "))
        result = a - b
        print(f"La diff est = {result}")

    elif choix == 3:
        a = float(input("Donner le premier nombre = "))
        b = float(input("Donner le deuxieme nombre = "))
        result = a * b
        print(f"La multiplication est = {result}")

    elif choix == 4:
        a = float(input("Donner le premier nombre = "))
        b = float(input("Donner le deuxieme nombre = "))
        if b == 0:
            print("Division impossible")
        else:
            result = a / b
            print(f"La division est = {result}")

    elif choix == 5:
        a = float(input("Donner le premier nombre = "))
        b = float(input("Donner le deuxieme nombre = "))
        result = a ** b
        print(f"La racine de a^b est = {result}")

    elif choix == 6:
        a = float(input("Donner nombre pour calculer la racine = "))
        if a >= 0:
            result = math.sqrt(a)
            print(f"La racine carre est = {result}")
        else:
            print("entrer un nombre positif seulement")

    elif choix == 7:
        a = float(input("Donner nombre pour calculer le carre = "))
        result = a ** 2
        print(f"Le carre est = {result}")

    elif choix == 8:
        a = float(input("Donner nombre pour calculer le cube = "))
        result = a ** 3
        print(f"Le cube du nombre est = {result}")

    elif choix == 9:
        a = float(input("Donner le nombre dont vous voulez sa val abs= "))
        result = abs(a)
        print(f"La valeur absolue est = {result}")

    elif choix == 10:
        a = int(input("Donner le premier nombre : "))
        b = int(input("Donner le deuxieme nombre : "))
        while b != 0:
            r = a % b
            a = b
            b = r
        print(f"Le PGCD est = {a}")

    elif choix == 11:
        a = int(input("Donner le nombre desirer a calculer son fact: "))
        if a == 0:
            print("0! = 1")
        else:
            facto = 1
            nb = a

            while nb > 0:
                facto = facto * nb
                nb = nb - 1

        print(f"La factorielle est = {facto}")

