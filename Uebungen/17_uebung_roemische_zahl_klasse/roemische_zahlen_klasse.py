# Klasse fuer roemische Zahlen

# Erstellen Sie eine Klasse RoemischeZahl.
# Die Klasse hat ein Attribut roemische_zahl_str, der im Konstruktor gesetzt wird.
# Die Klasse hat eine Methode konvertiere_zu_dezimal, die den Dezimalwert der römischen Zahl zurückgibt.
# Erzeugen Sie ein Objekt der Klasse und wenden darauf die Methode konvertiere_zu_dezimal an.

# Erinnerung
# Die Funktion zur Umwandlung sieht folgendermassen aus:

'''
def konvertiere_zu_dezimal(roemische_zahl_str):

    roem_to_dez_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 
    
    dezimal_zahl = 0
    prev = 0
    for zeichen in roemische_zahl_str:
        current = roem_to_dez_dict[zeichen]
        if prev < current:
            dezimal_zahl -= prev
        else:
            dezimal_zahl += prev
        prev = current
    dezimal_zahl += current

    return dezimal_zahl

'''

# Definition der Klasse
class RoemischeZahl:
    


# Anwendung der Klasse
roemische_zahl = RoemischeZahl('MCMLXVI')
dezimal_zahl = roemische_zahl.konvertiere_zu_dezimal()
print("Dezimalwert:", dezimal_zahl)
