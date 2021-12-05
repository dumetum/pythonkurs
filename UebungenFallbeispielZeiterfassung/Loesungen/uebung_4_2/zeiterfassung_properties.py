#
# Uebung 4.2: Properties
#


class Ereignis:
    def __init__(self, projekt_name, typ, zeitstempel):
        self.__projekt_name = projekt_name
        self.__typ = typ
        self.__zeitstempel = zeitstempel
        
    def set_projekt_name(self, projekt_name):
        self.__projekt_name = projekt_name
        
    def get_projekt_name(self):
        return self.__projekt_name
        
    projekt_name = property(get_projekt_name, set_projekt_name)
        
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
    
