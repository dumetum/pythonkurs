# Eingabe: Minuten (Bsp.: 136)
# Ausgabe: Stunden und Minuten (Bsp: 2 und 16)
#
# Erweitern Sie das Programm folgendermaßen:
#   Wenn eine negative Zahl eingegeben wird, soll eine entsprechende Ausgabe erfolgen.
#   In diesem Fall soll keine weitere Berechnung stattfinden.
#
# Zusatzaufgabe:
# 1) Wenn die eingegebenen Minuten mehr als ein Tag beträgt, machen Sie eine entsprechende Ausgabe
# 2) Wenn die Anzahl der Minuten mehr als ein Tag beträgt, geben Sie die Anzahl der Tage aus

minuten = int(input("Geben Sie die Minuten ein: "))

stunden = minuten // 60
minuten = minuten % 60

print("Stunden, Minuten: ", stunden, minuten)
