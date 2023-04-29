# Und das ist die Lösung von chatGPT.
# Zugegebenermassen etwas einfacher :-)

size = int(input("Geben Sie die Anzahl der Zeilen ein: "))

for i in range(size):
    for j in range(size):
        if i == j or i + j == size - 1:
            print('X', end='')
        else:
            print(' ', end='')
    print()