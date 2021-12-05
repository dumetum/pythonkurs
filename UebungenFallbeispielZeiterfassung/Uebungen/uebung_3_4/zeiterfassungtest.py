#
# Uebung 3.4: Hauptprogramm: Benutzung von Modul zeiterfassung:
#  Einlesen einer Liste von Ereignissen aus der Datei ereignisliste.txt
#  Berechnung der Arbeitszeit pro Projekt (und anschliessende Ausgabe)
#

# Erinnerung: Lösung aus Übung 3.1:
'''
ereignisliste = lese_ereignisliste_aus_datei("ereignisliste.txt")
arbeitszeit_dict = berechne_arbeitszeit_pro_projekt(ereignisliste)
for projekt, arbeitszeit in arbeitszeit_dict.items():
    arbeitszeit_stunde = arbeitszeit // 60
    arbeitszeit_minute = arbeitszeit % 60

    print("Vergangene Zeit für das Projekt " + projekt + ": " + str(arbeitszeit_stunde) + ":" + str(arbeitszeit_minute))    
'''

