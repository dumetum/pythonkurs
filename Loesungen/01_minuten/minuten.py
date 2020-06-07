# Eingabe: Minuten (Bsp.: 136)
# Ausgabe: Stunden und Minuten (Bsp: 2 und 16)

minuten = int(input("Geben Sie die Minuten ein: "))

stunden = minuten // 60
minuten = minuten % 60

print("Stunden, Minuten: ", stunden, minuten)
