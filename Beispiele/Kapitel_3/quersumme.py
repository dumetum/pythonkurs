 
zahl = int(input("Geben Sie eine ganze Zahl ein: "))

zahl_als_string = str(zahl)

quersumme = 0
for ziffern_zeichen in zahl_als_string:
    ziffer_wert = int(ziffern_zeichen)
    quersumme = quersumme + ziffer_wert
    
print("Die Quersumme ist:", quersumme)
