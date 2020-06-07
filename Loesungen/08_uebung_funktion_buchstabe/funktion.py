# Schreiben Sie eine Funktion berechne_anzahl, die als Eingabe einen Zeichenkette und einen Buchstaben bekommt
# und als Rückgabewert die Anzahl der Vorkommen des Buchstabens in der Zeichenkette ausgibt.

def berechne_anzahl(zeichenkette, buchstabe):
    anzahl_buchstabe_in_zeichenkette = 0     
    for zeichen in zeichenkette:
        if zeichen == buchstabe:
            anzahl_buchstabe_in_zeichenkette = anzahl_buchstabe_in_zeichenkette + 1
    return anzahl_buchstabe_in_zeichenkette
     
        
zeichenkette = input("Geben Sie eine Zeichenkette ein: ")
buchstabe = input("Geben Sie einen Buchstaben ein: ")
 
anzahl_buchstabe_in_zeichenkette = berechne_anzahl(zeichenkette, buchstabe)
         
         
print("Der Buchstabe '" + buchstabe + "' kommt in der Zeichenkette '" + zeichenkette + "' " + str(anzahl_buchstabe_in_zeichenkette) + "-mal vor.")
