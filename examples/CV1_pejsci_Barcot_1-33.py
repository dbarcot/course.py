# Tento program odpočítává pejsky s různými zprávami v závislosti na počtu.

# Získání číselného vstupu od uživatele a jeho převod na celé číslo (integer)
# Předpokládá se, že uživatel zadá platné celé číslo.
n = int(input("Zadejte počet pejsků: " ))

# Cyklus for pro odpočítávání od 'n' dolů do 1 (rozsah range(n, 0, -1) nezahrnuje koncovou hodnotu 0)
for i in range(n, 0, -1):
    # Podmíněné příkazy pro výpis různého textu na základě aktuální hodnoty 'i'
    if i == 1: # Pokud je počet pejsků 1
        print(f"{i} pejsek jde na výlet sám.")
    elif i in [2, 3, 4]: # Pokud je počet pejsků 2, 3 nebo 4
        print(f"{i} pejsci jdou na výlet, jeden se zaběhl.")
    else: # Pro všechny ostatní počty pejsků (5 a více)
        print(f"{i} pejsků jde na výlet a jeden se zaběhl.")

# Po dokončení cyklu program končí.
