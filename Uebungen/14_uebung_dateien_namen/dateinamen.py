# Schreiben Sie ein Programm, das aus der Datei datei_mit_namen.txt abwechselnd
# einen Vor- und einen Nachnamen liest und eine Datei namen_ausgabe.txt erstellt,
# in der pro Zeile Vor- und Nachname steht.
#
# Entnommen aus "Einführung in Python 3" von Bernd Klein, Hanser-Verlag.

eingabedatei = open("datei_mit_namen.txt", "r")
ausgabedatei = open("namen_ausgabe.txt","w")

aktueller_vorname = None
aktueller_nachname = None

for eingabe_zeile in eingabedatei:
    name = eingabe_zeile.strip()
    print("Aktueller Name in der Eingabedatei: " + name)
    
    # Hier geht es weiter



eingabedatei.close()
ausgabedatei.close()
