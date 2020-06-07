#
# Binäre Suche in einer geordneten Liste
#
# Idee: 
#   - Betrachte das Element in der Mitte:
#     - Das Element ist das gesuchte Element: Gebe den Index aus und fertig
#     - Das Element ist größer als das gesuchte Element: Suche (rekursiv) in der linken Hälfte der Liste
#     - Das Element ist kleiner als das gesuchte Element: Suche (rekursiv) in der rechten Hälfte der Liste
#
# Hinweis: Der Algorithmus kann iterativ und rekursiv implementiert werden.
#
# Zur iterativen Implementierung: Idee: Starte mit unten = 0 und oben = len(liste) - 1
# Schleife so lange oben >= unten bzw. Element noch nicht gefunden.
#  mitte = (oben+unten)//2
#  Teste Element an der Stelle mitte
#  Andernfalls ändere oben oder unten so dass nur noch in der entsprechenden Unterliste gesucht wird.
#
# s. auch https://idea-instructions.com/binary-search/

l = ["Andreas", "Anton", "Bernd", "Berta", "Christian", "Dagobert", "Doris", "Emil", "Thomas", "Xaver", "Yps"]

def bin_search(liste, element):
    # Gibt den Index des Elementes in der Liste zurueck.
    # Ist das Element nicht vorhanden, wird -1 zurueckgegeben



# Hauptprorgramm

print(str(l) + "\n")

# Es ist immer sinnvoll die Randfaelle abzupruefen:
print("AA: " + str(bin_search(l, "AA")))
print("Andreas: " + str(bin_search(l, "Andreas")))
print("Yps: " + str(bin_search(l, "Yps")))
print("YY: " + str(bin_search(l, "YY")))

# Und noch zwei Faelle in der Mitte. Einer mit Treffer und einer ohne
print("Christian: " + str(bin_search(l, "Christian")))
print("Chris: " + str(bin_search(l, "Chris")))
