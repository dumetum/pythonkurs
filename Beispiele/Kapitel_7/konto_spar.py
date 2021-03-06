# Die Idee der Kontoklasse stammt aus Johannes Ernesti, Peter Kaiser: Python 3, Das umfassende Handbuch, Rheinwerk Computing 

class Konto:

    def __init__(self, inhaber, kontonummer, kontostand = 0):
        self._inhaber = inhaber
        self._kontonummer = kontonummer
        self._kontostand = kontostand
    
    # Methode hat Zugriffsrecht protected, d.h. ist in Klasse und Unterklasse aufrufbar, aber nicht von außen
    def _pruefe_betrag(self,betrag):
        if betrag <= 0.0:
            raise Exception("Negativen Betrag nicht möglich!")
    
    def einzahlen(self, betrag):
        self._pruefe_betrag(betrag)
        self._kontostand += betrag        

    def auszahlen(self, betrag):
        self._pruefe_betrag(betrag)
        self._kontostand -= betrag

    def __str__(self):
        return "Inhaber: " + self._inhaber + ", Kontonummer: " + str(self._kontonummer) + ", Kontostand: " + str(self._kontostand)


class Sparkonto(Konto):
    
    def __init__(self, inhaber, kontonummer, zinssatz, kontostand = 0):
        super().__init__(inhaber, kontonummer, kontostand)   
        self.__zinssatz = zinssatz
    
    def berechne_zinsen_pro_jahr(self):
        # Das gilt natürlich nur,wenn sich der kontostand ein Jahr nicht ändert. Ist halt ein Festgeld-Sparkonto :-)
        return self.__zinssatz / 100 * self._kontostand
        
    def __str__(self):
        return super().__str__() + ", Zinssatz: " + str(self.__zinssatz)


if __name__ == "__main__":
    k = Sparkonto("Sabine", 4610, 0.5, 100.00)
    print(str(k) + ": Zinsen: " + str(k.berechne_zinsen_pro_jahr()))
    

