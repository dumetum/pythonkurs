#
# Uebung 3.3: Sortiere Liste von Ereignissen
#


# Beispielliste von Ereignissen aufbauen 
ereignis_1 =  ("Python-Kurs", "Start", (8,15))
ereignis_2 =  ("Python-Kurs", "Ende", (10,5))

ereignis_3 =  ("Java-Projekt", "Start", (10,20))
ereignis_4 =  ("Java-Projekt", "Ende", (11,30))

ereignis_5 =  ("Python-Kurs", "Start", (11,45))
ereignis_6 =  ("Python-Kurs", "Ende", (15,50))

ereignis_7 =  ("Java-Projekt", "Start", (16,0))
ereignis_8 =  ("Java-Projekt", "Ende", (18,30))

ereignis_liste = [ereignis_5, ereignis_8, ereignis_3, ereignis_1, ereignis_7, ereignis_2, ereignis_4, ereignis_6]


# Ausgabe der unsortierten Liste
print("Unsortierte Liste: ")
for ereignis in ereignis_liste:
    print(ereignis)
        

# Liste sortieren
# Erinnerung: eine Liste l kann sortiert werden mit l.sort(key = funktion_die_auf_die_Elemente_angewendet_wird)



# Ausgabe der sortierten Liste
print("Sortierte Liste: ")
for ereignis in ereignis_liste:
    print(ereignis)
