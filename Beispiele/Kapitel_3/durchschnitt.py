summe = 0
anzahl = 0
verbrauch = input("Geben Sie einen Verbrauch ein (oder ende): ")

while verbrauch != "ende":
    summe = summe + float(verbrauch)
    anzahl = anzahl + 1
    verbrauch = input("Geben Sie einen Verbrauch ein (oder ende): ")

durchschnitt = summe / anzahl
print(durchschnitt)
