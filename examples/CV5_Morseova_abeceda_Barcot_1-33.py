MORSEOVA_ABECEDA = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ",": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    "–": "–..–"
}


def prevest_na_morseovku(text):
    text = text.upper()  
    vysledek = ""  
    slovo_mezera = " || "  
    znak_mezera = " | "  

    prvni_slovo = True
    for slovo in text.split():  
        if not prvni_slovo:
            vysledek += slovo_mezera  
        prvni_slovo = False

        prvni_znak = True
        for znak in slovo:  
            if not prvni_znak:
                vysledek += znak_mezera  
            prvni_znak = False

            vysledek += MORSEOVA_ABECEDA.get(znak, "?")

    return vysledek

vstup = input("Zadejte text k převedení do Morseovy abecedy: ")
print(prevest_na_morseovku(vstup))

prevest_na_morseovku("A B")

slovo=["A","B"]
print(slovo[0])
