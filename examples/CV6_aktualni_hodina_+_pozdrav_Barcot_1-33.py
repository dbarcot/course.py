import time
dny = ["pondělí", "úterý", "středa", "čtvrtek", "pátek", "sobota", "neděle"]
mesice = ["ledna", "února", "března", "dubna", "května", "června", 
          "července", "srpna", "září", "října", "listopadu", "prosince"]

t = time.localtime()
hodina = t.tm_hour
den_v_tydnu = dny[t.tm_wday]
den = t.tm_mday
mesic = mesice[t.tm_mon - 1]
rok = t.tm_year
cas = time.strftime("%H:%M", t)

if 0 <= hodina <= 5:
    pozdrav = "Už jsi měl/a být v posteli!"
elif 6 <= hodina <= 11:
    pozdrav = "Dobré ráno!"
elif 12 <= hodina <= 17:
    pozdrav = "Dobré odpoledne!"
elif 18 <= hodina <= 21:
    pozdrav = "Dobrý večer!"
else:
    pozdrav = "Dobrou noc!"

print(pozdrav)
print(f"Dnes je {den_v_tydnu} {den}. {mesic} {rok}, {cas}")
