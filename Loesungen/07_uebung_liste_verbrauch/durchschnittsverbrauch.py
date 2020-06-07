# Gegeben sei die folgende Liste mit Verbrauchsdaten eines PKWs.
# Schreiben Sie ein Programm, das den Durchschnittsverbrauch berechnet.

verbrauchsdaten = [22.1, 34.2, 12.4, 45.2, 23.6, 33.2] 

anzahl_werte = 0
gesamtverbrauch = 0
for verbrauch in verbrauchsdaten:
    anzahl_werte = anzahl_werte + 1
    gesamtverbrauch = gesamtverbrauch + verbrauch
    
durchschnitt = gesamtverbrauch / anzahl_werte
print("Der Durchschnittsverbrauch ist ", durchschnitt)
    
