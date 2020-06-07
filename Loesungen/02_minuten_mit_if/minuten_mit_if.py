# Eingabe: Minuten (Bsp.: 136)
# Ausgabe: Stunden und Minuten (Bsp: 2 und 16)
#
# Erweitern Sie das Programm folgendermaßen:
# - Wenn eine negative Zahl eingegeben wird, soll eine entsprechende Ausgabe erfolgen.
#
# Zusatzaufgabe:
# 1) Wenn die eingegebenen Minuten mehr als ein Tag beträgt, machen Sie eine entsprechende Ausgabe
# 2) Wenn die Anzahl der Minuten mehr als ein Tag beträgt, geben Sie die Anzahl der Tage aus

minuten = int(input("Geben Sie die Minuten ein: "))

if minuten < 0:
    print("Sie haben eine negative Zahl eingegeben!")
else:
    tage = minuten // (60 * 24)
    rest_minuten = minuten % (60 * 24)
    stunden = rest_minuten // 60
    minuten = rest_minuten % 60

    print("Tage, Stunden, Minuten: ", tage, stunden, minuten)
    
    if tage > 0:
        print("Die Anzahl der eingegebenen Minuten ist also mehr als ein Tag!")
