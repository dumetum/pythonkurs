#
# Uebung 4.5: Hauptprogramm
#


import zeiterfassung_sort as z
    
ereignisliste = z.lese_ereignisliste_aus_datei("ereignisliste.txt")
ereignisliste.sort(key = z.Ereignis.sortier_kriterium)

for ereignis in ereignisliste:
    print(ereignis)
