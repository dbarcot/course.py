#Domácí úkol 2 - ovoce a zelenina
ovoce = ["jablko","hruska","merunka","tresen"]
zelenina = ["mrkev","celer","cibule","rajce"]

x = input ("Zadejte ovoce či zeleninu: ")
if x in ovoce:
    print("Zadal jste ovoce.")
elif x in zelenina:
    print("Zadal jste zeleninu.")
else:
    print("Toto slovo neznám.")
    
while True:
    pokracovat = input ("Chcete zadat nové slovo (a/n)? ")
    if pokracovat == "a":
        x = input ("Zadejte ovoce či zeleninu: ")
        if x in ovoce:
             print("Zadal jste ovoce.")
        elif x in zelenina:
             print("Zadal jste zeleninu.")
        else:
            print("Toto slovo neznám.")
    else:
        print("Děkujeme za použití programu")
        break