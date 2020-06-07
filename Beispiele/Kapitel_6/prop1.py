# Die get- und set-Methoden unten haben keinen besonderen Mehrwert

class Konto():

    def __init__(self, kontoinhaber):
        self.__kontostand = 0.0
        self.__kontoinhaber = kontoinhaber

    def set_kontoinhaber(self, kontoinhaber):
        self.__kontoinhaber = kontoinhaber

    def get_kontoinhaber(self):
        return self.__kontoinhaber

k = Konto("Maier")
print(k.get_kontoinhaber())
k.set_kontoinhaber("Schulz")
print(k.get_kontoinhaber())

