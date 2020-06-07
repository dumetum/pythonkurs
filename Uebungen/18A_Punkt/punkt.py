# Schreiben Sie eine Klasse, die einen (zweidimensionalen) Punkt
# repraesentiert (also mit x- und y-Koordinate).
# Es soll moeglich sein, zwei Punkte mit dem + Operator zu addieren.

class Punkt:
    pass
            
p1 = Punkt(1,2)
p2 = Punkt(3,4)
p3 = p1 + p2

print("Summe: " + str(p3))
