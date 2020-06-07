
roem_zahl_string = "XIV"

roem_to_dez_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 
dezimal_wert = 0
for  ziffer in roem_zahl_string:
    print("Bearbeite Ziffer", ziffer)
    
    wert_ziffer = roem_to_dez_dict[ziffer]
        
    print("Wert der Ziffer", wert_ziffer)
