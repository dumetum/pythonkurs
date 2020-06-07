
class Konto:

    anzahl = 0

    def __init__(self):
        Konto.anzahl += 1


if __name__ == "__main__":
    k1 = Konto()
    print(str(Konto.anzahl))

    k2 = Konto()
    print(str(Konto.anzahl))
