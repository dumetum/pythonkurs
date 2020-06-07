
anzahl_monate = int(input("Geben Sie die Anzahl der Monate an: "))

gesamt_verbrauch = 0

for i in range(1,anzahl_monate + 1):
    verbrauch_monat = float(input("Geben Sie den Verbrauch für Monat " + str(i) + " ein: ")) 
    gesamt_verbrauch = gesamt_verbrauch + verbrauch_monat
    
durchschnitt = gesamt_verbrauch / anzahl_monate
print("Der Durchschnittsverbrauch ist ", durchschnitt, " Liter.")
