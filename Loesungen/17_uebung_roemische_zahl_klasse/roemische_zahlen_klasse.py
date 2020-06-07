# Klasse fuer roemische Zahlen

class RoemischeZahl:
    
    def __init__(self, roemische_zahl_str):
        self.roemische_zahl_str = roemische_zahl_str
        
    def konvertiere_zu_dezimal(self):
    
        roem_to_dez_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 
        
        dezimal_zahl = 0
        prev = 0
        for zeichen in self.roemische_zahl_str:
            current = roem_to_dez_dict[zeichen]
            if prev < current:
                dezimal_zahl -= prev
            else:
                dezimal_zahl += prev
            prev = current
        dezimal_zahl += current

        return dezimal_zahl


roemische_zahl = RoemischeZahl('MCMLXVI')
dezimal_zahl = roemische_zahl.konvertiere_zu_dezimal()
print("Dezimalwert:", dezimal_zahl)
