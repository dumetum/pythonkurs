#
# Uebung 2.2: Teil 3
#
# Berechne die Arbeitszeit pro Projekt


# Beispielliste von Ereignissen aufbauen 
ereignis_1 =  ("Python-Kurs", "Start", (8,15))
ereignis_2 =  ("Python-Kurs", "Ende", (10,5))

ereignis_3 =  ("Java-Projekt", "Start", (10,20))
ereignis_4 =  ("Java-Projekt", "Ende", (11,30))

ereignis_5 =  ("Python-Kurs", "Start", (11,45))
ereignis_6 =  ("Python-Kurs", "Ende", (15,50))

ereignis_7 =  ("Java-Projekt", "Start", (16,0))
ereignis_8 =  ("Java-Projekt", "Ende", (18,30))

ereignis_liste = [ereignis_1, ereignis_2, ereignis_3, ereignis_4, ereignis_5, ereignis_6, ereignis_7, ereignis_8]

# Schritt 1: Dictionary aufbauen:
# Schluessel: Projektname
# Eintrag: Liste von Ereignissen für dieses Projekt
projekt_ereignis_list_dict = {}
for ereignis in ereignis_liste:
    projekt = ereignis[0]
    if projekt not in projekt_ereignis_list_dict:
        projekt_ereignis_list_dict[projekt] = [ereignis]
    else:
        projekt_ereignis_list_dict[projekt].append(ereignis)
        
# Schritt 2: Ueber Einträge dieses Dictionaries schleifen.
# Für jedes Projekt die Berechnung durchführen
for projekt, ereignis_liste in projekt_ereignis_list_dict.items():
    arbeitszeit_in_minuten = 0
    for ereignis in ereignis_liste:
        if ereignis[1] == "Start":
            start_stunde = ereignis[2][0]
            start_minute = ereignis[2][1]
        else:
            ende_stunde = ereignis[2][0]
            ende_minute = ereignis[2][1]
            arbeitszeit_in_minuten = arbeitszeit_in_minuten + ((ende_stunde * 60 + ende_minute) - (start_stunde * 60 + start_minute))    
    arbeitszeit_stunde = arbeitszeit_in_minuten // 60
    arbeitszeit_minute = arbeitszeit_in_minuten % 60

    print("Vergangene Zeit für das Projekt " + projekt + ": " + str(arbeitszeit_stunde) + ":" + str(arbeitszeit_minute))
