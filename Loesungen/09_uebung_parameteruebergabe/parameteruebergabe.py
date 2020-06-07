# Schreiben Sie eine Funktion, die in einer Liste alle Vorkommen von 8 durch 16 ersetzt.
# Die Funktion soll die Anzahl der Ersetzungen zurueckgeben

def ersetze(liste):
    anzahl = 0
    index = 0
    for element in liste:
        if element == 8:
            liste[index] = 16
            anzahl = anzahl + 1
        index = index + 1
    return anzahl
    
l = [2,4,8,5,8,3]
print("Liste vor dem Funktionsaufruf: ", l)

anzahl_8 = ersetze(l)
print("Es wurden", anzahl_8, "Vorkommen von 8 durch 16 ersetzt")
print("Liste nach dem Funktionsaufruf: ", l)
