name_zu_anzahl_dict = {}
while True:
    name = input("Geben Sie einen Namen ein: ")
    if name == "Ende":
        break
    if name in name_zu_anzahl_dict:
        name_zu_anzahl_dict[name] += 1
    else:
        name_zu_anzahl_dict[name] = 1

for name in name_zu_anzahl_dict:
    print("Der Name", name, "ist", name_zu_anzahl_dict[name] , "mal eingegeben worden.")