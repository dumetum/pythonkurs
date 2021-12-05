#
# Uebung 3.5: Ausnahmen
#
# Die Funktion berechne_arbeitszeit soll eine Ausnahme werfen, wenn die Reihenfolge der Ereignisse nicht korrekt ist.
# Die Funktion berechne_arbeitszeit_pro_projekt soll die Ausnahme abfangen und in diesem Fall eine Fehlermeldung ausgeben
#  und eine -1 als Arbeitszeit für das Projekt in das Ergebnis-Dictionary schreiben
#


def anzahl_minuten_nach_mitternacht(ereignis):
    return ereignis[2][0] * 60 + ereignis[2][1]
    

def zeitdifferenz(zeittupel1, zeittupel2):
    return (zeittupel1[0] * 60 + zeittupel1[1] - zeittupel2[0] * 60 - zeittupel2[1])
    

# Die Funktion soll eine Ausnahme werfen, wenn die Reihenfolge der Ereignisse nicht korrekt ist.    
def berechne_arbeitszeit(ereignisliste):
    ereignisliste.sort(key = anzahl_minuten_nach_mitternacht)
    arbeitszeit_in_minuten = 0
    for ereignis in ereignisliste:        
        if ereignis[1] == "Start":
            startzeittupel = (ereignis[2][0], ereignis[2][1])
        else:
            endezeittupel = (ereignis[2][0], ereignis[2][1])
            arbeitszeit_in_minuten = arbeitszeit_in_minuten + zeitdifferenz(endezeittupel, startzeittupel)  
    return arbeitszeit_in_minuten
 

# Die Funktion soll die Ausnahme abfangen und in diesem Fall eine Fehlermeldung ausgeben
#  und eine -1 als Arbeitszeit für das Projekt in das Ergebnis-Dictionary schreiben
def berechne_arbeitszeit_pro_projekt(ereignisliste):    
    projekt_ereignis_list_dict= {}
    for ereignis in ereignisliste:
        projekt = ereignis[0]
        if projekt not in projekt_ereignis_list_dict:
            projekt_ereignis_list_dict[projekt] = [ereignis]
        else:
            projekt_ereignis_list_dict[projekt].append(ereignis)    

    projekt_arbeitszeit_dict = {}
    for projekt, projekt_ereignis_liste in projekt_ereignis_list_dict.items():
        arbeitszeit_fuer_projekt = berechne_arbeitszeit(projekt_ereignis_liste)
        projekt_arbeitszeit_dict[projekt] = arbeitszeit_fuer_projekt
        
    return projekt_arbeitszeit_dict
        
        
def lese_ereignisliste_aus_datei(dateiname):
    ereignis_liste = []
    fobj = open(dateiname, "r")
    for line in fobj:
        bestandteile = line.strip().split(",")
        ereignis_liste.append((bestandteile[0].strip(), bestandteile[1].strip(), (int(bestandteile[2]), int(bestandteile[3])))) 
    return ereignis_liste
    
