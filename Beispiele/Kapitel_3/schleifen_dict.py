d = {"eins":1, "zwei":2, "drei": 3}

# Schleife ueber die Schluessel
for key in d:
    print(key)

# Schleife ueber die Schluessel-Wert-Paare
for key, value in d.items():
    print("Schlüssel: ", key, "Wert: ", value)

# Schleife ueber die Werte    
for value in d.values():
    print(value)