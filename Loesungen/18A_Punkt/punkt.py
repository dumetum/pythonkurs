# Schreiben Sie eine Klasse, die einen (zweidimensionalen) Punkt
# repraesentiert (also mit x- und y-Koordinate).
# Es soll moeglich sein, zwei Punkte mit dem + Operator zu addieren.

class Punkt:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
       
    def __str__(self):
        return "(" + str(self.__x) + "," + str(self.__y) + ")"
       
    def __add__(self, other):
        if type(other) == Punkt:
            return Punkt(self.__x + other.__x, self.__y + other.__y)
        else:
            raise Exception("Fehler: Addition eines Punktes mit einem Objekt vom Typ: " + str(type(other)))
            
p1 = Punkt(1,2)
p2 = Punkt(3,4)
p3 = p1 + p2

print("Summe: " + str(p3))

x = p1 + 1
