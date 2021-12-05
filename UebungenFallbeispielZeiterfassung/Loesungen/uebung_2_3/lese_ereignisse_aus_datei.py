#
# Übung 2.3: Lese Ereignisse aus Datei
#

# Die Datei ereignisliste.txt enthält Zeilen der folgenden Form:
# Python-Kurs, Start, 8, 15

# Die Ereignisse sollen in Tupel gelesen werden:
# (Projektname, Projekttyp, (Startstunde, Startminute))

# Ergebnisliste mit Ereignissen:
ereignis_liste = []

fobj = open("ereignisliste.txt", "r")
for line in fobj:
    bestandteile = line.strip().split(",")
    ereignis_liste.append((bestandteile[0].strip(), bestandteile[1].strip(), (int(bestandteile[2]), int(bestandteile[3])))) 
    
# Schleife über die Liste und Ausgabe der Ereignisse
for ereignis in ereignis_liste:
    print(ereignis)
