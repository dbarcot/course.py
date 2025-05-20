import math # Import modulu math pro přístup k matematickým funkcím a konstantě pi

# Definice funkce pro převod stupňů na radiány
def stupne_na_radiany(stupne):
    # Vzorec pro převod: stupně * (PI / 180)
    return stupne * math.pi / 180

# Definice funkce pro převod radiánů na stupně
def radiany_na_stupne(radiany):
    # Vzorec pro převod: radiány * (180 / PI)
    return radiany * 180 / math.pi

# Definice funkce pro výpis menu možností
def vypis_menu():
    print("\nNabídka:") # Vypíše prázdný řádek a nadpis menu
    print("---")
    print("1 ... převod na radiány")
    print("2 ... převod na stupně")
    print("3 ... konec programu")
    print("---")

# Definice funkce pro načtení a validaci volby uživatele
def nacti_volbu():
    # Nekonečný cyklus, dokud uživatel nezadá platnou volbu
    while True:
        volba = input("Tvoje volba: ") # Získá vstup od uživatele
        try:
            volba = int(volba) # Pokusí se převést vstup na celé číslo
            # Kontrola, zda je číslo v platném rozsahu (1, 2 nebo 3)
            if 1 <= volba <= 3:
                return volba # Pokud je platné, vrátí číslo a ukončí cyklus
            else:
                print("Neplatna volba!!!") # Chybová zpráva pro neplatné číslo
        except ValueError:
            print("Musis stisknout cislo!") # Chybová zpráva, pokud vstup nebyl číslo

# Definice funkce pro provedení samotného převodu na základě volby
def proved_prevod(volba):
    if volba == 1: # Pokud uživatel zvolil převod na radiány
        # Nekonečný cyklus pro získání platného číselného vstupu
        while True:
            try:
                stupne = float(input("Zadej úhel ve stupních: ")) # Získá vstup a pokusí se převést na desetinné číslo
                radiany = stupne_na_radiany(stupne) # Zavolá funkci pro převod
                print(f"{stupne:.3f}° je {radiany:.3f}rad") # Vypíše výsledek formátovaný na 3 desetinná místa
                break # Ukončí vnitřní cyklus po úspěšném převodu a výpisu
            except ValueError:
                print("Zadejte platné číslo!") # Chybová zpráva, pokud vstup nebyl číslo
    elif volba == 2: # Pokud uživatel zvolil převod na stupně
        # Nekonečný cyklus pro získání platného číselného vstupu
        while True:
            try:
                radiany = float(input("Zadej úhel v radiánech: ")) # Získá vstup a pokusí se převést na desetinné číslo
                stupne = radiany_na_stupne(radiany) # Zavolá funkci pro převod
                print(f"{radiany:.3f}rad je {stupne:.3f}°") # Vypíše výsledek formátovaný na 3 desetinná místa
                break # Ukončí vnitřní cyklus po úspěšném převodu a výpisu
            except ValueError:
                print("Zadejte platné číslo!") # Chybová zpráva, pokud vstup nebyl číslo


# Hlavní smyčka programu
while True:
    vypis_menu() # Zavolá funkci pro zobrazení menu
    volba = nacti_volbu() # Zavolá funkci pro načtení a validaci volby

    if volba == 3: # Pokud uživatel zvolil konec (volba 3)
        break # Ukončí hlavní nekonečný cyklus programu
    else: # Pokud uživatel zvolil převod (volba 1 nebo 2)
        proved_prevod(volba) # Zavolá funkci pro provedení převodu
