# Uebung 2.1: Differenz zweier Uhrzeiten unter Verwendung von +, - und if

stunde_1=8
minute_1=15

stunde_2=10
minute_2=5

# Berechnung der Differenz: diff_stunde und diff_minute
if minute_2 >= minute_1:
    diff_minute = minute_2 - minute_1
    diff_stunde = stunde_2 - stunde_1
else:
    diff_minute = 60 + minute_2 - minute_1
    diff_stunde = stunde_2 - stunde_1 - 1
    
    
# Ausgabe: Wenn Uhrzeit 2 VOR Uhrzeit 1, soll eine entsprechende Fehlermeldung ausgegeben werden    
if diff_stunde < 0:
    print("Fehler: Uhrzeit 2 ist vor Uhrzeit 1")
else:
    print("Vergangene Zeit: " + str(diff_stunde) + ":" + str(diff_minute))
