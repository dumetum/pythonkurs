satz = "Dies ist ein langer Satz mit Nebensatz"

aktuelle_laenge = 0
maximale_laenge = 0

for zeichen in satz:
    if zeichen == " ":
        print("Wortende gefunden. Länge aktuelles Wort:", aktuelle_laenge)
        print("Bisherige maximale Länge:", maximale_laenge)
        if aktuelle_laenge > maximale_laenge:
            maximale_laenge = aktuelle_laenge
        aktuelle_laenge = 0
    else:
        aktuelle_laenge += 1

# Das letzte Wort (nicht abgeschlossen mit Leerzeichen) könnte das längste Wort sein
print("Wortende gefunden. Länge aktuelles Wort:", aktuelle_laenge)
print("Bisherige maximale Länge:", maximale_laenge)
if aktuelle_laenge > maximale_laenge:
    maximale_laenge = aktuelle_laenge

print("Die maximale Länge ist:", maximale_laenge)
