# Datenstruktur zum Speichern mehrerer Ereignisse

# Ereignisse als Tupel
ereignis_1 =  ("Python-Kurs", "Start", (8,15))
ereignis_2 =  ("Python-Kurs", "Ende", (10,5))


# Mehrere Ereignisse: Liste von Tupeln
ereignis_liste = [ereignis_1, ereignis_2]

print("Zeit erstes Ereignis", ereignis_liste[0][2])
print("Stunde erstes Ereignis", ereignis_liste[0][2][0])


