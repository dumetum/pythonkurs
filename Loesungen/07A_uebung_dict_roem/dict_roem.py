# Schreiben Sie ein Programm, das als Eingabe eine Symbol einer roemischen Zahl erhaehlt und als Ausgabe die zugehoerige Zahl ausgibt.
# Verwenden Sie dazu ein Dictionary
# Dabei gilt:
#   'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000

roem_to_dez_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 

roem_symbol = input("Geben Sie ein Symbol einer roemischen Zahl ein: ")

print("Der Wert des Symbols", roem_symbol, "ist", roem_to_dez_dict[roem_symbol])
