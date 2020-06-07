# Schreiben Sie ein Programm, das aus der Datei datei_mit_namen.txt abwechselnd
# einen Vor- und einen Nachnamen liest und eine Datei namen_ausgabe.txt erstellt,
# in der pro Zeile Vor- und Nachname steht.
#
# Aus "Einführung in Python 3" von Bernd Klein, Hanser-Verlag.

eingabedatei = open("datei_mit_namen.txt", "r")
ausgabedatei = open("namen_ausgabe.txt","w")

aktueller_vorname = None
aktueller_nachname = None

for eingabe_zeile in eingabedatei:
    name = eingabe_zeile.strip()
    print("Aktueller Name in der Eingabedatei: " + name)
    
    if aktueller_vorname == None:
        # Wir sind in einer Zeile mit einem Vornamen. Diesen merken wir uns für den nächsten Schleifendurchlauf
        aktueller_vorname = name
    else:
        # Wir sind mit einer Zeile mit einem Nachnamen. Wir können einen kompletten Namen in die Ausgabedatei schreiben
        aktueller_nachname = name
        ausgabezeile = aktueller_vorname + " " + aktueller_nachname + "\n"
        print("Die folgende Zeile wird ind die Ausgabedatei geschrieben: " + ausgabezeile)
        ausgabedatei.write(ausgabezeile)
        # Der aktuelle Vorname wurde verwendet. Um dies für den nächsten Schleifedurchlauf kenntlich zu machen,
        # wird die Variable auf None zurückgesetzt
        aktueller_vorname = None

eingabedatei.close()
ausgabedatei.close()
