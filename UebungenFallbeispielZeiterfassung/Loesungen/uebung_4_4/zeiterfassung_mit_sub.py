#
# Uebung 4.4: Sub-Methode
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
            
    def __sub__(self, other):
        if type(other) != type(self):
            raise Exception("Unerlaubter Typ " + str(type(other)))
        if self.__typ != "Ende" or other.__typ != "Start":
            raise Exception("Differenzbildung nur erlaubt für Ende-Ereignis minus Start-Ereignis")
        if self.__projekt_name != other.__projekt_name:
            raise Exception("Die Ereignisse gehören nicht zu demselben Objekt")            
        return self.__zeitstempel[0] * 60 + self.__zeitstempel[1] - other.__zeitstempel[0] * 60 - other.__zeitstempel[1]
 
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
    
