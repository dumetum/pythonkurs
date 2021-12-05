#
# Uebung 3.1: Berechne Zeitaufwand für eine Liste von Ereignissen, die aus einer Datei gelesen werden.
# Benutze dazu Funktionen.
#

# Erinnerung: Code zum Lesen aus einer Datei
# (Anmerkung: Alle Zeilen zwischen ''' und ''' werden vom Interpreter als Kommentar ignoriert):

'''
    ereignis_liste = []
    fobj = open(dateiname, "r")
    for line in fobj:
        bestandteile = line.strip().split(",")
        ereignis_liste.append((bestandteile[0].strip(), bestandteile[1].strip(), (int(bestandteile[2]), int(bestandteile[3])))) 
'''

# Erinnerung: Code zum Berechnen der Gesamtarbeitzeit aus einer Liste von Ereignissen, unabhaengig vom Projekt
'''
    arbeitszeit_in_minuten = 0
    for ereignis in ereignisliste:
        if ereignis[1] == "Start":
            startzeittupel = (ereignis[2][0], ereignis[2][1])
        else:
            endezeittupel = (ereignis[2][0], ereignis[2][1])
            arbeitszeit_in_minuten = arbeitszeit_in_minuten + (endezeittupel[0] * 60 + endezeittupel[1] - startzeittupel[0] * 60 - startzeittupel[1])
'''

# Optional: Erinnerung: Code zum Berechnen der Arbeitszeit pro Projekt aus einer Liste von Ereignissen:

'''
   projekt_ereignis_list_dict= {}
    for ereignis in ereignisliste:
        projekt = ereignis[0]
        if projekt not in projekt_ereignis_list_dict:
            projekt_ereignis_list_dict[projekt] = [ereignis]
        else:
            projekt_ereignis_list_dict[projekt].append(ereignis)    

    projekt_arbeitszeit_dict = {}
    for projekt, projekt_ereignis_liste in projekt_ereignis_list_dict.items():
        arbeitszeit_fuer_projekt = HIER SOLLTE JETZT DER CODE OBEN VERWENDET WERDEN. VIELLEICHT VIA EINER FUNKTION :-)
        projekt_arbeitszeit_dict[projekt] = arbeitszeit_fuer_projekt
'''


#
# Hier kommen die Funktionen
#

# Funktion: 
#  Eingabe: Dateiname
#  Rückgabe: Liste von Ereignissen


# Funktion
#  Eingabe: Liste von Ereignissen
#  Rückgabe: Gesamtarbeitszeit ueber alle Ereignisse

# Optional: Funktion:
#  Eingabe: Liste von Ereignissen
#  Ausgabe: Dictionary:
#    Schluessel: Projektname
#    Wert: Arbeitszeit fuer dieses Projekt

    
#    
# Hauptprogramm
#

# Ereignisliste aus Datei einlesen
ereignisliste = 

# Arbeitszeiten pro Projekt ausrechnen

