#
# Uebung 3.5: Hauptprogramm
#  Der fuer die Uebung anzupassende Code ist in der Datei zeiterfassung_mit_ausnahme.py
#

import zeiterfassung_mit_ausnahme as z
    
ereignisliste = z.lese_ereignisliste_aus_datei("ereignisliste.txt")
arbeitszeit_dict = z.berechne_arbeitszeit_pro_projekt(ereignisliste)

for projekt, arbeitszeit in arbeitszeit_dict.items():
    if arbeitszeit != -1:
        arbeitszeit_stunde = arbeitszeit // 60
        arbeitszeit_minute = arbeitszeit % 60

        print("Vergangene Zeit für das Projekt " + projekt + ": " + str(arbeitszeit_stunde) + ":" + str(arbeitszeit_minute))    
