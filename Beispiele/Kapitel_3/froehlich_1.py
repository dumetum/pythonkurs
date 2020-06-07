# Die Idee der "fröhlichen Zahlen" stammt aus: https://ccd-school.de/coding-dojo/

zahl = int(input("Geben Sie eine Zahl ein: "))

while zahl != 1:
    zahl_str = str(zahl)
    zahl = 0
    for ziffer_str in zahl_str:
        zahl = zahl + int(ziffer_str) ** 2
    print("Neue Zahl: " + str(zahl))
    input()
    
