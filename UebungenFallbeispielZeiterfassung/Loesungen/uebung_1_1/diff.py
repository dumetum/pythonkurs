# Uebung 1.1: Differenz zweier Uhrzeiten

stunde_1=8
minute_1=15

stunde_2=10
minute_2=5

# Berechnung der Differenz
anzahl_minuten_1 = stunde_1 * 60 + minute_1
anzahl_minuten_2 = stunde_2 * 60 + minute_2

diff_in_minuten = anzahl_minuten_2 - anzahl_minuten_1

# Ausgabe in Stunde / Minute
diff_stunde = diff_in_minuten // 60
diff_minute = diff_in_minuten % 60

print("Vergangene Zeit: " + str(diff_stunde) + ":" + str(diff_minute))
