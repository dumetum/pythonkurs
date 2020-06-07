# Die Idee der "fröhlichen Zahlen" stammt aus: https://ccd-school.de/coding-dojo/

zahl = int(input("Geben Sie eine Zahl ein: "))
gepruefte_zahlen = []

while zahl not in gepruefte_zahlen and zahl != 1:
    gepruefte_zahlen.append(zahl)
    zahl_str = str(zahl)
    zahl = 0
    for ziffer_str in zahl_str:
        zahl += int(ziffer_str) ** 2
    print("Neue Zahl: " + str(zahl))
    
        
if zahl == 1:
    print("Fröhlich!")
else:
    print("Nicht fröhlich")
