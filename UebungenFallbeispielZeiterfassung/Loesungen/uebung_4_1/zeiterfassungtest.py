#
# Uebung 4.1: Hauptprogramm
#  Der fuer die Uebung anzupassende Code ist in der Datei zeiterfassung_mit_klassen.py
#

import zeiterfassung_mit_klassen as z
    
ereignisliste = z.lese_ereignisliste_aus_datei("ereignisliste.txt")

for ereignis in ereignisliste:
    print("Ereignis: ", ereignis)
