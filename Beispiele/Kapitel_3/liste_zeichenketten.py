 
anzahl = int(input("Anzahl der zu verarbeitenden Zeichenketten: "))

zeichenketten = []
for i in range(1,anzahl+1):
    s = input("Geben Sie den " + str(i) + "-ten String ein: ")
    zeichenketten.append(s)
    
for s in zeichenketten:
    print(s)
