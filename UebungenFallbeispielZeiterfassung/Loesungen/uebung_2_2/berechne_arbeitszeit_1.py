#
# Uebung 2.2: Teil 1
#
# Schleife über Liste mit Ereignissen.
# Berechne die Gesamtarbeitszeit (unabhängig vom Projekt)

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


# Schleife über ereignis_liste
# Erinnerung: Arbeitszeit zwischen Start und Ende erhält man am einfachsten, indem man die Zeiten in Minuten umrechnet
arbeitszeit_in_minuten = 0
for ereignis in ereignis_liste:
    if ereignis[1] == "Start":
        start_stunde = ereignis[2][0]
        start_minute = ereignis[2][1]
    else:
        ende_stunde = ereignis[2][0]
        ende_minute = ereignis[2][1]
        arbeitszeit_in_minuten = arbeitszeit_in_minuten + ((ende_stunde * 60 + ende_minute) - (start_stunde * 60 + start_minute))
        

# Ausgabe in Stunde / Minute
# Erinnerung: Aus den Minuten erhält man die Stunden durch ganzzahlige Division (//) und die Minuten über den Rest (%)
arbeitszeit_stunde = arbeitszeit_in_minuten // 60
arbeitszeit_minute = arbeitszeit_in_minuten % 60

print("Vergangene Zeit: " + str(arbeitszeit_stunde) + ":" + str(arbeitszeit_minute))

