alter = int(input("Alter des Mitglieds: "))
anzahl_abteilungen = int(input("Anzahl der Abteilungen des Mitglieds: "))

beitrag = 60 + 20 * anzahl_abteilungen

if alter > 60:
    beitrag = beitrag * 0.8
if alter <= 18:
    beitrag = beitrag * 0.5

print("Mitgliedsbeitrag:", beitrag, "EUR")

input('press Return>')
