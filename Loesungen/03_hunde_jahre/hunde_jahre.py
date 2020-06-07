# Schreiben Sie ein Programm, das das Alter eines Hundes in Menschenjahren ausgibt.
# Eingabe: Alter des Hundes
# Ausgabe: Entsprechends Alter in Menschenjahren
# Berechnung:
#  Ein einjähriger Hund entspricht etwa einem 14-jährigen Menschen
#  2 Hundejahren entsprechen etwa 22 Menschenjahren
#  Ab dann entspricht ein Hundejahr jeweils 5 Menschenjahren
# 
# aus Bernd Klein: "Einführung in Python 3", Hanser-Verlag

alter_des_hundes = int(input("Alter des Hundes: "))

if alter_des_hundes == 1:
    menschen_jahre = 14
elif alter_des_hundes == 2:
    menschen_jahre = 22
elif alter_des_hundes > 2:
    menschen_jahre = 22 + (alter_des_hundes -2 ) * 5

print("Menschenjahre:", menschen_jahre)
