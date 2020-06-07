# Umwandlung roemische Zahlen in Dezimalzahlen
#
# Verwenden Sie das Modul roemische_zahlen zur Umwandlung
# einer roemischen Zahl in eine Dezimalzahl
import roemische_zahlen as r

roem_zahl_str = 'MCMLXVI'
dezimal_zahl = r.roemisch_zu_dezimal(roem_zahl_str)
print("Dezimalwert:", dezimal_zahl)

roem_zahl_str = input("Geben Sie eine roemische Zahl ein: ")
dezimal_zahl = r.roemisch_zu_dezimal(roem_zahl_str)
print("Dezimalwert:", dezimal_zahl)
