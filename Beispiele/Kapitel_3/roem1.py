
roem_zahl_string = "XIV"

dezimal_wert = 0
for  ziffer in roem_zahl_string:
    print("Bearbeite Ziffer", ziffer)
    
    wert_ziffer = 0
    
    if ziffer == 'M':
        wert_ziffer = 1000
    elif ziffer  == 'D':
        wert_ziffer = 500
    elif ziffer  == 'C':
        wert_ziffer = 100
    elif ziffer  == 'L':
        wert_ziffer = 50
    elif ziffer  == 'X':
        wert_ziffer = 10
    elif ziffer  == 'V':
        wert_ziffer = 5
    elif ziffer  == 'I':
        wert_ziffer = 1
        
    print("Wert der Ziffer", wert_ziffer)
