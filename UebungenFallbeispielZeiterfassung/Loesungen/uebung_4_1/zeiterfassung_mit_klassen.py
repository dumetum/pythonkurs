#
# Uebung 4.1: Klassen
#


# Klasse Ereignis mit den Attributen projekt_name, typ, zeitstempel
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
    
