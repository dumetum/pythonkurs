import roem6_mod

while True:
    roem_zahl_str = input("Geben Sie eine roemische Zahl ein (Ende zum Beenden): ")
    if roem_zahl_str == "Ende":
        break
    dezimal_wert = roem6_mod.berechne_dezimalwert_einer_roem_zahl(roem_zahl_str)
    print("Der Dezimalwert der roemischen Zahl", roem_zahl_str, "beträgt", dezimal_wert)
