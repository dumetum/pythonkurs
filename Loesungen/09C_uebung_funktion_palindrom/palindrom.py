# Schreiben Sie eine Funktion, die fuer einen Eingabestring prueft, ob es
# sich um ein Palindrom handelt (ergibt von vorne und von hinten gelesen das gleiche
# Ergebnis, z.B. Anna
# (Nach Bernd Klein, Einfuehrung in Python)

def ist_palindrom(wort):
    rueckgabe = True
    index = 0
    while index < len(wort)//2:
        if wort[index] != wort[-index - 1]:
            rueckgabe = False
            break
        index = index + 1
    return rueckgabe

wort = input("Geben Sie ein Wort ein: ")
while wort != "ende":
    print("Die Aussage 'Das Wort",  wort, "ist ein Palindrom' ist", ist_palindrom(wort))
    wort = input("Geben Sie ein Wort ein: ")