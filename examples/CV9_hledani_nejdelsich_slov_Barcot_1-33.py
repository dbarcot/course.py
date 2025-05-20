def najdi_nejdelsi_slova(soubor):
    try:
        with open(soubor, 'r', encoding='utf-8') as f:
            slova = []
            for radek in f:
                
                radek = radek.replace('„', ' ').replace('“', ' ').replace(',', ' ').replace('.', ' ')
                slova.extend(radek.split())
            
            
            max_delka = max(len(slovo) for slovo in slova)
            nejdelsi = [slovo for slovo in slova if len(slovo) == max_delka]
            
            return max_delka, nejdelsi
    
    except FileNotFoundError:
        print(f"Soubor '{soubor}' nebyl nalezen!")
        return None, []

delka, slova = najdi_nejdelsi_slova('moudra.txt')
if slova:
    print(f"Nejdelší slovo má {delka} znaků:")
    print("Jedná se o následující slova:", slova)