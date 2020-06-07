
roem_zahl_string = "XIV"

roem_to_dez_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 

dezimal_wert = 0
vorgaenger_wert_ziffer = 0

for  ziffer in roem_zahl_string:
    print("Bearbeite Ziffer", ziffer)    
    aktueller_wert_ziffer = roem_to_dez_dict[ziffer]
    print("Wert der aktuellen Ziffer", aktueller_wert_ziffer)
    
    # Jetzt kann entschieden werden, ob der Vorgaengerwert addiert oder subtrahiert werden muss
    if vorgaenger_wert_ziffer < aktueller_wert_ziffer:
        dezimal_wert = dezimal_wert - vorgaenger_wert_ziffer
    else:
        dezimal_wert = dezimal_wert + vorgaenger_wert_ziffer
        
    # Der Vorgaengerwert für den naechsten Schleifendurchlauf ist der aktuelle Wert dieses Schleifendurchlaufs
    vorgaenger_wert_ziffer = aktueller_wert_ziffer
    
# Nach dem die Schleife komplett durchlaufen ist, muss noch der letzte Wert addiert werden,
# da in der Schleife selbst ja immer nur die Vorgaengerwerte addiert / subtrahiert werden.
# Der letzte Wert wird immer addiert, da keine Ziffer mehr folgt (und damit insbesondere auch keine groessere
dezimal_wert = dezimal_wert + aktueller_wert_ziffer

print("Der Dezimalwert ist", dezimal_wert)
