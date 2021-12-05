#
# Uebung 4.5: Hauptprogramm
# - Implementieren Sie in zeiterfassung_sort.py in der Klasse Ereignis die Methode sortier_kriterium
# - Benutzen Sie diese hier, um die Liste zu sortieren
#


import zeiterfassung_sort as z
    
ereignisliste = z.lese_ereignisliste_aus_datei("ereignisliste.txt")

# Liste sortieren:
# ereignisliste.sort ...

for ereignis in ereignisliste:
    print(ereignis)
