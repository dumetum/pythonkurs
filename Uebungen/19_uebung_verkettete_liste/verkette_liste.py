
class Knoten:

    def __init__(self, inhalt):
        self.inhalt = inhalt
        self.naechster_knoten = None


class VerketteteListe:

    def __init__(self):
        self.__start_knoten = None

    def __str__(self):
        knoten = self.__start_knoten
        ausgabe_string = ''
        while knoten:
            ausgabe_string += (str(knoten.inhalt) + " - ")
            knoten = knoten.naechster_knoten
        return ausgabe_string

    def einfuegen(self, inhalt):
        pass

    def loeschen(inhalt):
        pass

    def enthaelt(inhalt):
        pass

l = VerketteteListe()
l.einfuegen(1)
l.einfuegen(2)
print(str(l))

