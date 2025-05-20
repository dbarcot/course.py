import math

def stupne_na_radiany(stupne):
    return stupne * math.pi / 180

def radiany_na_stupne(radiany):
    return radiany * 180 / math.pi

def vypis_menu():
    print("Nabídka:")
    print("---")
    print("1 ... převod na radiány")
    print("2 ... převod na stupně")
    print("3 ... konec programu")
    print("---")

def nacti_volbu():
    while True:
        volba = input("Tvoje volba: ")
        try:
            volba = int(volba)
            if 1 <= volba <= 3:
                return volba
            else:
                print("Neplatna volba!!!")
        except ValueError:
            print("Musis stisknout cislo!")

def proved_prevod(volba):
    if volba == 1:
        while True:
            try:
                stupne = float(input("Zadej úhel ve stupních: "))
                radiany = stupne_na_radiany(stupne)
                print(f"{stupne:.3f}° je {radiany:.3f}rad")
                break
            except ValueError:
                print("Zadejte platné číslo!")
    elif volba == 2:
        while True:
            try:
                radiany = float(input("Zadej úhel v radiánech: "))
                stupne = radiany_na_stupne(radiany)
                print(f"{radiany:.3f}rad je {stupne:.3f}°")
                break
            except ValueError:
                print("Zadejte platné číslo!")


while True:
    vypis_menu()
    volba = nacti_volbu()
    if volba == 3:
        break
    else:
        proved_prevod(volba)