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

# Erinnerung 1: Die Kommandozeilenparameter sind in der Liste sys.argv verfuegbar.
# Dabei gilt: sys.argv[0] ist der Programmname, also "start.py".
# Dann folgen die weiteren Parameter.

# Erinnerung 2: Schreiben in eine Datei:
# fobj = open(“ausgabedatei“,“a+“) # Damit wird an eine bestehende Datei angehangen, wenn diese existiert.
# fobj.write(“Zeile1\n“)
# fobj.write(“Zeile2\n“)
# fobj.close

