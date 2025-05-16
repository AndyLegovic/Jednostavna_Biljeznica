open("Jednostavna_Bilježnica.txt", "w").close()
radi = True
while radi:
    print("--- Jednostavna Bilježnica ---")
    print("1.Dodaj novu bilješku")
    print("2.Pregledaj sve bilješke")
    print("3.Izlaz\n")
    opcija = int(input("Odaberite opciju 1-3:"))

    if opcija == 1:
        bilj = input("Unesi bilješku")
        with open("Jednostavna_Bilježnica.txt", "a") as bilježnica:
            bilj += "\n"
            bilježnica.write(bilj)
            print("Bilješka je uspješno spremljena")

    elif opcija == 2:
        with open("Jednostavna_Bilježnica.txt", "r") as bilježnica:
            sadrzaj = bilježnica.read()
            if not sadrzaj:
                print("Bilježnica je prazna")
            else:
                print(sadrzaj)

    elif opcija == 3:
        radi = False
        print("Doviđenja!")
    else:
        print("Neispravan odabir. Molimo unesite broj između 1 i 3.")