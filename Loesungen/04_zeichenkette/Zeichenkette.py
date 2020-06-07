# Eingabe: Eine Zeichenkette und zwei ganze Zahlen i und f
# Das Programm soll f mal das i-te Zeichen ausgeben
#
# Was passiert, wenn Sie einen Index angeben, der außerhalb des Bereichs der Zeichenkette liegt?
# Verhindern Sie dies durch eine Abfrage.
#
# Was passiert, wenn Sie einen negativen Faktor eingeben?



s = input("Geben Sie eine Zeichenkette ein: ") 
i = int(input("Geben Sie einen Index ein: "))
f = int(input("Geben Sie einen Faktor ein: "))

if i >= len(s) or i < 0:
    print("Der Index ist nicht erlaubt")
else:
    erg = s[i] * f
    print(erg)


