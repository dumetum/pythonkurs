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
# Hinweis: Test, ob ein Schlüssel in einem Dictionary vorhanden ist: if projekt in projekt_ereignis_list_dict:
# Hinweis: Anängen eines neuen Elements e an eine Liste l: l.append(e)

projekt_ereignis_list_dict = {}

        
# Schritt 2: Ueber Einträge dieses Dictionaries schleifen.
# Für jedes Projekt die Berechnung durchführen
# Hinweis: Über Schlüssel, Wert-Paare eines Dictionaries schleift man folgendermaßen:
# for projekt, ereignis_liste in projekt_ereignis_list_dict.items():
