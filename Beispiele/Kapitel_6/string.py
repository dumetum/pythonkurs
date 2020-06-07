# Die Idee, die Objektorientierung an Hand einer Kontoklasse einzuführen, stammt aus dem Buch
# Johannes Ernesti,Peter Kaiser: Python 3, Das umfassende Handbuch, Rheinwerk Computing 

class Konto:

    def __init__(self, kontoinhaber, kontostand):
        self.__kontoinhaber = kontoinhaber
        self.__kontostand = kontostand

    def __str__(self):
        return "Kontoinhaber: " + self.__kontoinhaber + ", Kontostand: " + str(self.__kontostand)

k = Konto("Maier", 100.0)
print(str(k))
