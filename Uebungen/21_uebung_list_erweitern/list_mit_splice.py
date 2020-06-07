# Aus: Bernd Klein: Einführung in Python 3 
#
# Schreiben Sie eine Klasse MeineListe, die die unten angegebene Klasse PList um eine Methode splice erweitert:
# splice(offset, length, replacement)
# „offset” entspricht dem ersten Index, ab dem die Elemente gelöscht werden sollen, und der Parameter „length” gibt an, 
# wie viele Elemente gelöscht werden sollen. 
# An die Stelle der gelöschten Elemente sollen die Elemente der Liste replacement eingefügt werden.
#


# Definition der Klasse Plist:
class PList(list):
    def __init__(self, list):
        super().__init__(list)
        
    def push(self, element):
        self.append(element)
        
        
# Hier Definition der Klasse MeineListe, die von PList ableitet und
# die Methode splice zur Verfügung stellt


# Verwendung der Klasse MeineListe
if __name__ == "__main__":
    x = MeineListe([33,456,8,34,99])
    x.push(47)
    print(x)
    x.splice(2,3,["Hey", "you"])
    print(x)
