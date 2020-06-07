# Beispiel: Verwendung einer "Flagge"

# Aufgabe: Bestimme in einer Liste von ganzen Zahlen,
# ob eine negative Zahl vorkommt

liste = [5,9,-1,10]

es_gibt_negativen_wert = False
for wert in liste:
    if wert < 0:
        es_gibt_negativen_wert = True
        break
        
if es_gibt_negativen_wert:
    print("Es gibt (mindestens) einen negativen Wert")
else:
    print("Alle Zahlen in der Liste sind positiv oder null")
    
    
