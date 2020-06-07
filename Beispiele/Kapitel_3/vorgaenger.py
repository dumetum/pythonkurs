# Beispiel: In einem Schleifendurchlauf wird ein Wert
# aus dem vorhergehendem Schleifendurchlauf benoetigt

# Aufgabe: Bestimme in einer Liste von ganzen Zahlen, wie
# oft eine groessere Zahl vor einer kleineren Zahl steht.
#
# Beispiel: In der Liste [2,5,9,8,10] ist das einmal der Fall:
# die 9 steht vor der 8

liste = [2,5,9,8,10]
vorgaenger_wert = None
anzahl = 0

for aktueller_wert in liste:
    # Zu der folgenden if-Abfrage beachte den Kommentar unten
    if (vorgaenger_wert != None) and (vorgaenger_wert > aktueller_wert):
        anzahl += 1
    vorgaenger_wert = aktueller_wert
    
print("In der Liste kommt es " +  str(anzahl) + " mal vor, dass eine groessere Zahl vor einer Kleineren steht!")

# zur if-Anweisung:
# 1) Der Ausdruck hinter dem if wird von links nach rechts ausgewertet. Hat die Variable vorgaenger_wert den Wert None so ist
#    diese Bedingung "falsch". Die Und-Verknüpfung von "falsch" mit irgendetwas ist immer "falsch". Daher wird in diesem
#    Fall der Ausdruck (vorgaenger_wert > aktueller_wert) gar nicht ausgewertet. Was in diesem Fall auch gar nicht ginge,
#    da None > zahl keinen Sinn ergibt und nicht erlaubt ist.
# 2) Das None-Objekt wird in booleschen Ausdrücken (also in solchen, bei denen das Ergebnis wahr oder falsch ist)
#    wie "falsch" interpretiert. Die if-Anweisung könnte also auch abkürzend folgendermaßen geschrieben werden:
#    if vorgaenger_wert and vorgaenger_wert > aktueller_wert:

