#
# Uebung 4.4: Sub-Methode: Fürgen Sie zur Klasse Ereignis die Sub-Methode hinzu
#


class Ereignis:
    def __init__(self, projekt_name, typ, zeitstempel):
        self.__projekt_name = projekt_name
        self.__typ = typ
        self.__zeitstempel = zeitstempel
        
    def __str__(self):
        # Das könnte man noch schöner machen:
        # - Wenn die Minuten einstellig sind, dann zweistellig ausgeben: z.B. 12:05h statt 12:5h
        # - Formatieren, so dass alle Ausgaben passend untereinander stehen (s. format-Methode)
        return "Projektname: " + self.__projekt_name + ", Typ: " + self.__typ + ", Zeitstempel: " + str(self.__zeitstempel[0]) + ":" + str(self.__zeitstempel[1]) + "h."
            
    # Einfügen der Sub-Methode
    # Ausnahme werfen (raise Exception("Sprechende Fehlermeldung")) wenn:
    # - das zu subtrahierende Objekt kein Objekt vom Typ Ereignis ist
    # - nicht die Differenz eines Ende-Ereignisses und eines Start-Ereignisses gebildet wird.
    # - die beiden Ereignisse nicht zum selben Projekt gehören
    # Erinnerung: Differenz: Stunden_ereignis_1 * 60 + Minuten_ereignis_1 - Stunden_ereignis_2 * 60 - Minuten_ereignis_2

 
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
    
