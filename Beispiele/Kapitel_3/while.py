
i = 1

gesamt_verbrauch = 0
while i <= 6:
    verbrauch_monat = float(input("Geben Sie den Verbrauch für Monat " + str(i) + " ein: ")) 
    gesamt_verbrauch = gesamt_verbrauch + verbrauch_monat
    i = i + 1
    
durchschnitt = gesamt_verbrauch / 6
print("Der Durchschnittsverbrauch ist ", durchschnitt, " Liter.")
