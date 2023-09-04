int_rom=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
double = {"CM" : 900, "CD" : 400, "XC" : 90, "XL" : 40, "IX" : 9, "IV" : 4}
unique = {"M" : 1000, "D" : 500, "C" : 100, "L" : 50, "X" : 10, "V" : 5, "I" : 1}
singles = ["V","L","D"]
triples = ["I","X","D"]

def nb_to_roman(n):
    roman = ""
    for i, num in int_rom:
        while n >= i:
            n -= i
            roman += num
    return roman

def roman_to_nb(roman):
    entier = 0
    i = 0
    while i < len(roman):
        if i < len(roman) - 1 and roman[i:i+2] in double:
            entier += double[roman[i:i+2]]
            i += 2
        else:
            entier += unique[roman[i]]
            i += 1
    return entier

def verif_roman(roman):
    return all(x in unique.keys() for x in roman)

def is_decreasing(sequence):
    length = len(sequence)
    for i in range(length - 2):
        if sequence[i] < sequence[i + 1] < sequence[i + 2]:
            return False
    return True

def verif_croissant_roman(roman):
    roman_values = [roman_to_nb(x) for x in roman]
    return roman in double.keys() or is_decreasing(roman_values)

def verif_mulitple_same_element(element, liste):
    return liste.count(element) < 2

def verif_multiple_same_letter(roman,nb_same,liste):
    return any(roman.count(x) > nb_same-1 for x in roman if x in liste)

def sum_roman(somme):
    if "+" in somme:
        nbs = [x.replace(" ","") for x in somme.split("+")]
        for x in nbs:
            if not verif_roman(x):
                return "Impossible, Il y a des lettres qui ne signifient aucun nombre dans ma base de donnée"
            if not verif_croissant_roman(x):
                return "Impossible, les lettres ne sont pas décroissantes"
            for nb in [2,4]:
                if verif_multiple_same_letter(x,nb,singles):
                    return f"Impossible, il y a une des lettres: {[singles,triples][nb/2-1]} qui se répètent au moins {nb} fois dans votre calcul"
        nb = sum([roman_to_nb(x) for x in nbs])
        if not (nb >= 1 and nb <= roman_to_nb("MMMCMXCIX")):
            return "Impossible, il faut que l'opération soit entre I et MMMCMXCIX"
        return nb_to_roman(nb)
    if " " in somme:
        return "Impossible le programme ne prend en compte que l'addition"
    if " " not in somme:
        return "Impossible, pour faire une addition il me faut 2 éléments"

tests = ["X + IV","MXCIX + CIV","II + II","MMMCX + DCII",
         "MCMXCIX + I", "IVM + I", "VVI", "XXXX", "TX",
         "XX - IV", "IV", "MMMCMXC + X"]

for x in tests:
    print(f"{x} = {sum_roman(x)}")
