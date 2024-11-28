print("Üdvözlöm!")

def feladatos():
    feladatok = []
    while True:

        print("Ez a program egy To-Do lista. Kérjük válasszon az alábbi opciók közül:")
        print("1: Új feladat hozzáadása")
        print("2: Feladatlista kiírása")
        print("3: Kilépés a programból")
        v = int(input("/: "))

        if v == 1:
            feladat = input("Add meg a feladatot: ")
            feladatok.append(feladat)
            print(f"'{feladat}' hozzáadva a listához")
        elif v == 2:
            print(feladatok)
            print(f'{len(feladatok)} feladat van.')
        elif v == 3:
            print("Adatok feltöltése a felhőbe...")
            exit()
        else:
            print('Érvénytelen válasz')
feladatos()

