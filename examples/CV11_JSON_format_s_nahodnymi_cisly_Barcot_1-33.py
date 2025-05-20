import random
import json

# Vytvoření seznamu měření
mereni = []

for i in range(1, 11):  # 10 měření
    cisla = [random.randint(0, 100) for _ in range(10)]  # 10 náhodných čísel
    mereni.append({
        "poradi": i,
        "cisla": cisla
    })

# Zabalení do hlavního objektu
vystup = {"mereni": mereni}

# Uložení do JSON souboru
with open("mereni.json", "w") as soubor:
    json.dump(vystup, soubor, indent=4)
