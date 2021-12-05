#
# Uebung 4.3: Hauptprogramm
#

import zeiterfassung_mit_str as z
    
ereignisliste = z.lese_ereignisliste_aus_datei("ereignisliste.txt")

for ereignis in ereignisliste:
    print(ereignis)
 
