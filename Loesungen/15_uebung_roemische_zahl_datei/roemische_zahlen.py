# Umwandlung roemische Zahlen in Dezimalzahlen
#
# Lesen der roemischen Zahlen aus einer Datei und Schreiben der Ergebnisse in eine
# andere Datei

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

eingabedatei = open("roem.txt","r")
ausgabedatei = open("dezimal.txt", "w")

for line in eingabedatei:
    roem_zahl_str = line.strip()
    dezimal_zahl = roemisch_zu_dezimal(roem_zahl_str)

    print("Dezimalwert:", dezimal_zahl)
    ausgabedatei.write(str(dezimal_zahl) + "\n")
    
eingabedatei.close()
ausgabedatei.close()
