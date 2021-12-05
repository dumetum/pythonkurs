#
# Uebung 4.2: Properties
#


# Die Attribute der Klasse sollen als "privat" deklariert werden
# Für das Attribut projekt_name soll eine get- und eine set-Methode definiert werden
# Für das Attribut sollen properties definiert werden, so dass im Hauptprogramm ein Zugriff via
#   print("Projekt: ", ereignis.projekt_name)
# möglich ist.
class Ereignis:
    def __init__(self, projekt_name, typ, zeitstempel):
        self.projekt_name = projekt_name
        self.typ = typ
        self.zeitstempel = zeitstempel
        
# Funktion lese_ereignisliste_aus_datei(dateiname)
def lese_ereignisliste_aus_datei(dateiname):
    ereignis_liste = []
    fobj = open(dateiname, "r")
    for line in fobj:
        bestandteile = line.strip().split(",")
        name = bestandteile[0].strip()
        typ = bestandteile[1].strip()
        zeitstempel = (int(bestandteile[2]), int(bestandteile[3]))
        # Ereignis-Objekt erzeugen und in die Liste einfügen
        ereignis = Ereignis(name, typ, zeitstempel)
        ereignis_liste.append(ereignis) 
    return ereignis_liste
    
