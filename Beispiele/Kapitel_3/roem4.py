roem_to_dez_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 

while True:
    roem_zahl_str = input("Geben Sie eine roemische Zahl ein (Ende zum Beenden): ")
    if roem_zahl_str == "Ende":
        break
    
    dezimal_wert = 0
    vorgaenger_wert_ziffer = 0

    for  ziffer in roem_zahl_str:
        aktueller_wert_ziffer = roem_to_dez_dict[ziffer]        
        if vorgaenger_wert_ziffer < aktueller_wert_ziffer:
            dezimal_wert = dezimal_wert - vorgaenger_wert_ziffer
        else:
            dezimal_wert = dezimal_wert + vorgaenger_wert_ziffer            
        vorgaenger_wert_ziffer = aktueller_wert_ziffer        
    dezimal_wert = dezimal_wert + aktueller_wert_ziffer
    
    print("Der Dezimalwert der roemischen Zahl", roem_zahl_str, "beträgt", dezimal_wert)
