# Schreiben Sie eine Funktion berechne_max_wortlaenge:
#
# Parameter: Eine Zeichenkette, die einen Satz darstellt, z.B.
#          "Dies ist ein langer Satz mit Nebensatz"
# Rückgabe: Die Länge des längsten Wortes des Satzes. Im Beispiel also 9
#
# Testen Sie die Funktion an Hand der unten angegebenen Beispiele

# Im folgenden zur Erinnerung die Lösung ohne Funktion

# aktuelle_laenge = 0
# maximale_laenge = 0
# 
# for zeichen in satz:
#     if zeichen == " ":
#         if aktuelle_laenge > maximale_laenge:
#             maximale_laenge = aktuelle_laenge
#         aktuelle_laenge = 0
#     else:
#         aktuelle_laenge += 1
# 
# if aktuelle_laenge > maximale_laenge:
#     maximale_laenge = aktuelle_laenge



#
# Schreiben Sie hier die Funktion
#



#
# Testaufrufe
#
print(berechne_max_wortlaenge(""))
print(berechne_max_wortlaenge("Wort"))
print(berechne_max_wortlaenge("Langes Wort steht vorne"))
print(berechne_max_wortlaenge("Langes Wort steht ganzhinten"))
print(berechne_max_wortlaenge("Langes Wort steht alslangeswort in der Mitte"))