mitgliederliste = []
anzahl = int(input("Wieviele Mitglieder wollen Sie eingeben: "))
nummer = 0
while nummer < anzahl:
   nummer = nummer + 1
   neues_mitglied = input("Geben Sie den Namen des Mitgliedes ein: ")
   if neues_mitglied in mitgliederliste:
       print("Dieses Mitglied gibt es schon!")
   else: mitgliederliste.append(neues_mitglied)
   
print("Es gibt", len(mitgliederliste), "Mitglieder!")

       