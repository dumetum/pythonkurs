# Schreiben Sie ein Programm, das als Eingabe einen Zeichenkette und einen Buchstaben bekommt
# und als Ausgabe die Anzahl der Vorkommen des Buchstabens in der Zeichenkette ausgibt.
 
zeichenkette = input("Geben Sie eine Zeichenkette ein: ")
buchstabe = input("Geben Sie einen Buchstaben ein: ")
 
anzahl_buchstabe_in_zeichenkette = 0
 
for zeichen in zeichenkette:
    if zeichen == buchstabe:
        anzahl_buchstabe_in_zeichenkette = anzahl_buchstabe_in_zeichenkette + 1
         
         
print("Der Buchstabe '" + buchstabe + "' kommt in der Zeichenkette '" + zeichenkette + "' " + str(anzahl_buchstabe_in_zeichenkette) + "-mal vor.")
