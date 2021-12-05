#
# Uebung 2.2: Teil 2
#
# Wenn auf ein Start-Ereignis ein Ende-Ereignis folgt: continue
# Wenn auf ein Start-Ereignis ein Ereignis eines anderen Projektes folgt: break
# Berechne die Gesamtarbeitszeit (unabhängig vom Projekt)


# Beispielliste von Ereignissen aufbauen 
ereignis_1 =  ("Python-Kurs", "Start", (8,15))
ereignis_2 =  ("Python-Kurs", "Ende", (10,5))

ereignis_3 =  ("Java-Projekt", "Start", (10,20))
ereignis_3a =  ("Java-Projekt", "Start", (10,21))
ereignis_4 =  ("Java-Projekt", "Ende", (11,30))

ereignis_5 =  ("Python-Kurs", "Start", (11,45))
ereignis_6 =  ("Python-Kurs", "Ende", (15,50))

ereignis_7 =  ("Java-Projekt", "Start", (16,0))
ereignis_7a =  ("Python-Kurs", "Start", (16,5))
ereignis_8 =  ("Java-Projekt", "Ende", (18,30))

ereignis_liste = [ereignis_1, ereignis_2, ereignis_3, ereignis_3a, ereignis_4, ereignis_5, ereignis_6, ereignis_7, ereignis_7a, ereignis_8]


# Schleife über ereignis_liste
arbeitszeit_in_minuten = 0
letztes_projekt = None
letzter_typ = None
fehler = False

for ereignis in ereignis_liste:
    aktuelles_projekt = ereignis[0]
    aktueller_typ = ereignis[1]
        
    if letztes_projekt and letzter_typ and letzter_typ == "Start":
        if letztes_projekt != aktuelles_projekt:
            print("Fehler: auf Start-Ereignis von projekt " + letztes_projekt + " folgt ein Ereignis von Projekt " + aktuelles_projekt)
            fehler = True
            break
        if aktueller_typ != "Ende":
            print("Ein Start-Ereignis, das auf ein Start-Ereignis folgt, wird übersprungen!" + str(ereignis[2]))
            continue
    
    if ereignis[1] == "Start":
        start_stunde = ereignis[2][0]
        start_minute = ereignis[2][1]
    else:
        ende_stunde = ereignis[2][0]
        ende_minute = ereignis[2][1]
        arbeitszeit_in_minuten = arbeitszeit_in_minuten + ((ende_stunde * 60 + ende_minute) - (start_stunde * 60 + start_minute))
    
    letztes_projekt = aktuelles_projekt
    letzter_typ = aktueller_typ
        

# Ausgabe in Stunde / Minute
# Erinnerung: Aus den Minuten erhält man die Stunden durch ganzzahlige Division (//) und die Minuten über den Rest (%)

if fehler:
    print("Während der Verarbeitung ist ein Fehler aufgetreten!")
else:
    arbeitszeit_stunde = arbeitszeit_in_minuten // 60
    arbeitszeit_minute = arbeitszeit_in_minuten % 60

    print("Vergangene Zeit: " + str(arbeitszeit_stunde) + ":" + str(arbeitszeit_minute))

