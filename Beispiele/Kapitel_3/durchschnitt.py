summe = 0
anzahl = 0
verbrauch = float(input("Geben Sie einen Verbrauch ein: "))

while verbrauch >= 0:
    summe = summe + verbrauch
    anzahl = anzahl + 1
    verbrauch = float(input("Geben Sie einen Verbrauch ein"))

durchschnitt = summe / anzahl
print("Der Durchschnittsverbrauch ist: ", durchschnitt)