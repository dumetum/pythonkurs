
# Schreiben Sie ein Programm, das in einer Endlosschleife eine Eingabe entgegen nimmt:
# - Bei der Eingabe von Ende soll das Programm beendet werden.
# - Bei einer fehlerhaften Eingabe soll eine entsprechende Meldung ausgegeben werden und mit der nächsten Eingabe fortgefahren werden.

# Umwandlung einer roemischen Zahl in eine Dezimalzahl
def roemisch_zu_dezimal(roem_zahl_str):
    roem_to_dez_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 
    
    dezimal_zahl = 0
    prev = 0
    for zeichen in roem_zahl_str:
        current = roem_to_dez_dict[zeichen]
        if prev < current:
            dezimal_zahl -= prev
        else:
            dezimal_zahl += prev
        prev = current
    dezimal_zahl += current

    return dezimal_zahl

while True:
    roem_zahl_str = input("Geben Sie eine roemische Zahl ein: ")
    
