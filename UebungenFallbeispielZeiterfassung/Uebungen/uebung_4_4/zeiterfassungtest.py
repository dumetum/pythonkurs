#
# Uebung 4.4: Hauptprogramm
# - Fügen Sie in zeiterfassung_mit_sub die Sub-Methode hinzu
# - Testen Sie hier die Sub-Methode
#

import zeiterfassung_mit_sub as z
    
ereignisliste = z.lese_ereignisliste_aus_datei("ereignisliste.txt")

vor_ereignis = None
for ereignis in ereignisliste:
    print(ereignis)
    try:
        print("Differenz der letzten beiden Ereignisse ", str(ereignis - vor_ereignis))
    except Exception as e:
        print("Ausnahme: ", e)
    
    vor_ereignis = ereignis
 
