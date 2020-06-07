
# Definition einer Funktion:
# Eingabewert: Roemische Zahl als Zeichenkette
# Ausgabe: Wert der roemischen Zahl als ganze Zahl
def berechne_dezimalwert_einer_roem_zahl(roem_zahl_string):
    roem_to_dez_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 

    dezimal_wert = 0
    vorgaenger_wert_ziffer = 0

    for  ziffer in roem_zahl_string:
        aktueller_wert_ziffer = roem_to_dez_dict[ziffer]        
        if vorgaenger_wert_ziffer < aktueller_wert_ziffer:
            dezimal_wert = dezimal_wert - vorgaenger_wert_ziffer
        else:
            dezimal_wert = dezimal_wert + vorgaenger_wert_ziffer            
        vorgaenger_wert_ziffer = aktueller_wert_ziffer        
    dezimal_wert = dezimal_wert + aktueller_wert_ziffer

    return dezimal_wert

