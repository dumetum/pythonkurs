#
# Uebung 4.3: Hauptprogramm
#  Der fuer die Uebung anzupassende Code ist in der Datei zeiterfassung_mit_str.py
#

import zeiterfassung_mit_str as z
    
ereignisliste = z.lese_ereignisliste_aus_datei("ereignisliste.txt")

for ereignis in ereignisliste:
    print(ereignis)
    
