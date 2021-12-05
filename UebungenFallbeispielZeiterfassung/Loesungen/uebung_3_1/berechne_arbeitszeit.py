#
# Uebung 3.1: Berechne Zeitaufwand für eine Liste von Ereignissen, die aus einer Datei gelesen werden.
# Benutze dazu Funktionen.
#

# Zeitdifferenz in Minuten von zwei Tupeln der Form (Stunde, Minute)
def zeitdifferenz_in_minuten(zeittupel1, zeittupel2):
    return (zeittupel1[0] * 60 + zeittupel1[1] - zeittupel2[0] * 60 - zeittupel2[1])
    

# Arbeitszeit für eine Liste von Ereignissen unabhängig vom Projekt   
# Annahme: Die Liste der Ereignisse ist zeitlich korrekt sortiert 
# Rückgabe: Arbeitszeit in Minuten
def berechne_arbeitszeit(ereignisliste):
    arbeitszeit_in_minuten = 0
    for ereignis in ereignisliste:
        if ereignis[1] == "Start":
            startzeittupel = (ereignis[2][0], ereignis[2][1])
        else:
            endezeittupel = (ereignis[2][0], ereignis[2][1])
            arbeitszeit_in_minuten = arbeitszeit_in_minuten + zeitdifferenz_in_minuten(endezeittupel, startzeittupel)  
    return arbeitszeit_in_minuten
 

# Arbeitszeit pro Projekt für eine Liste von Ereignissen für verschiedene Projekte
# Annahme: Die Liste der Ereignisse ist zeitlich korrekt sortiert 
# Rückgabe: Dictionary: Projektname - Arbeitszeit in Minuten für das Projekt
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
 
        
# Einlesen einer Liste von Ereignissen aus einer Datei
def lese_ereignisliste_aus_datei(dateiname):
    ereignis_liste = []
    fobj = open(dateiname, "r")
    for line in fobj:
        bestandteile = line.strip().split(",")
        ereignis_liste.append((bestandteile[0].strip(), bestandteile[1].strip(), (int(bestandteile[2]), int(bestandteile[3])))) 
    return ereignis_liste
    
    
# Hauptprogramm
ereignisliste = lese_ereignisliste_aus_datei("ereignisliste.txt")
arbeitszeit_dict = berechne_arbeitszeit_pro_projekt(ereignisliste)
for projekt, arbeitszeit in arbeitszeit_dict.items():
    arbeitszeit_stunde = arbeitszeit // 60
    arbeitszeit_minute = arbeitszeit % 60

    print("Vergangene Zeit für das Projekt " + projekt + ": " + str(arbeitszeit_stunde) + ":" + str(arbeitszeit_minute))    
