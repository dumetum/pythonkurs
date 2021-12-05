# Uebung 3.2 Erzeugen Sie beim Aufruf dieses Programms via
#  python start.py projekt stunde minute
# Einen Zeile in der Datei ereignisliste.txt der Art
#  projekt, Start, Stunde, Minute
#
# Beispiel: Ein Aufruf von 
#  python start.py python-projekt 10 30
# erzeugt eine Zeile
#  python-projekt, Start, 10, 30

# Import des benoetigten Moduls
import sys

fobj = open("ereignisliste", "a+")
fobj.write(sys.argv[1] + ", Start, " + str(sys.argv[2]) + ", " + str(sys.argv[3]) + "\n")
fobj.close()
