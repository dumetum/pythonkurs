mitgliederliste = []

neues_mitglied = input("Geben Sie den Namen des Mitgliedes ein: ")
while neues_mitglied != "ende":
   if not (neues_mitglied in mitgliederliste):
       mitgliederliste.append(neues_mitglied)
   neues_mitglied = input("Geben Sie den Namen des Mitgliedes ein: ")
   
print("Es gibt", len(mitgliederliste), "Mitglieder!")

       