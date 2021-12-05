#
# Uebung 4.2: Hauptprogramm
#  Der fuer die Uebung anzupassende Code ist in der Datei zeiterfassung_properties.py
#

import zeiterfassung_properties as z
    
ereignisliste = z.lese_ereignisliste_aus_datei("ereignisliste.txt")

for ereignis in ereignisliste:
    print("Ereignis: ", ereignis)
    print("Projekt: ", ereignis.projekt_name)
