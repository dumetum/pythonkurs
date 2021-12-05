#
# Übung 2.3: Lese Ereignisse aus Datei
#

# Die Datei ereignisliste.txt enthält Zeilen der folgenden Form:
# Python-Kurs, Start, 8, 15

# Die Ereignisse sollen in Tupel gelesen werden:
# (Projektname, Projekttyp, (Startstunde, Startminute))

# Schleife über die Zeilen der Datei
# Erzeuge pro Zeile ein Tupel der obigen Form für ein Ereignis.
# Dazu muss die Zeile in die Bestandteile (durch Kommatas separiert) getrennt werden:
# Wenn zeile ein String ist, dann geht das mit: 
#   bestandteile = zeile.strip().split(",")
# bestandteile enthält dann eine Liste der Elemente der Zeile, also im Beispiel: bestandteile[0] ist "Python-Kurs" etc.
# Hänge das Ereignis an die Liste via:
# ereignis_liste.append(ereignis)


# Ergebnisliste mit Ereignissen
ereignis_liste = []

    
# Schleife über die Liste und Ausgabe der Ereignisse
