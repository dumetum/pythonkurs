# Pythonkurs für Programmieranfänger

Das Repository enthält Unterlagen für einen Pythonkurs für Programmieranfänger<sup>1</sup>. Diese beinhalten:

* Folien (Asciidoc und PDF)
* Beispiele
* Übungen (Vorlagen zur Bearbeitung und Lösungsvorschläge)

Die Unterlagen sind für ein Sebststudium nur bedingt geeignet. 
Sie sind als begleitende Unterlagen zu einer Präsenzveranstaltung gedacht.

## Zielgruppe

Während es bei einem Buch möglich ist, mehrere Zielgruppen im Auge zu haben, ist das bei einem Kurs eher nicht sinnvoll. Bei einem Buch können Personen mit Programmiererfahrung Kapitel weglassen oder überfliegen und Anfänger können bei Schwierigkeiten ein Kapitel mehrfach lesen. Bei einem Kurs wird man keiner Zielgruppe gerecht, wenn man versucht, alle Bedürfnisse abzudecken.

Der vorliegende Kurs ist daher explizit für Menschen ohne Programmierkenntnisse gedacht.

## Inhalt

Ziel des Kurses ist eine Einführung in die Programmierung mit der Programmiersprache Python. Algorithmen und allgemeine Programmierprinzipien werden nur am Rande behandelt.

Ebenso werden keine Werkzeuge (IDEs, Debugging, Unit-Tests) vorgestellt, da das Erlernen der Programmierung an sich im Vordergrund steht.

Natürlich kann der Kurs keine vollständige Einführung in die Sprache bieten. Die Teilnehmer sollen befähigt werden, weitere Schritte selbständig mit Büchern oder dem Internet durchzuführen.

Behandelt werden die folgenden Themen:
* Einführung in die Programmierung
* Datentypen
* Variablen, Zuweisungen, Verzweigungen, Schleifen
* Funktionen, Module und Pakete
* Grundlegendes Arbeiten mit Dateien
* Einführung in die Objektorientierung und Vererbung


## Zeitlicher Rahmen

Ich habe den Kurs bisher im Rahmen von 5 Terminen à 4 (Schul-) Stunden (3 Zeitstunden) gehalten. Dies war ausreichend - auch für die Bearbeitung der Übungen während des Kurses.

Da sich vier Stunden allerdings als sehr lange und fordernd (sowohl für den Dozenten als auch die Teilnehmer) herausgestellt hat, wird der Kurs künftig an 6 Terminen à 3 (Schul-) Stunden stattfinden.

Wenn dann am Ende das Thema Objektorienierung nicht vollständig behandelt werden kann, ist das in meinen Augen für einen Anfängerkurs nicht so schlimm.


## Hinweise zum Gebrauch

Wie beschrieben sind die Folien nur bedingt zum Selbststudium geeignet. In den Folien wird durch Symbole darauf hingewiesen, wo insbesondere ergänzende Erläuterungen durch den Vortragenden notwendig sind.

Die Beispiele (auch gekennzeichnet durch ein Symbol) sind oft nicht in die Folien integriert, sondern werden direkt in einem Editor oder einer IDE am „lebenden Objekt" demonstriert.

Die Übungen (zumindest zu jedem Thema eine) sollten während der Kurszeit bearbeitet werden. Zum einen werden die Übungen zu Hause sowieso nicht gemacht, zum anderen ist pure Theorie im Kurs (gerade für Anfänger) überfordernd (und auch für den Dozenten anstrengend).

Es gibt jeweils einen Ordner als Vorlage zur Bearbeitung der Übung, in dem schon ein Rahmen vorgegeben ist, damit die Bearbeitung während des Kurses einfacher ist, und einen Ordner mit einem Lösungsvorschlag.

Die Demonstration der Beispiele und die Bearbeitung der Übungsaufgaben kann mit einem einfachen Texteditor erfolgen. Sinnvoll sind Editoren mit Syntaxhervorhebung und der Möglichkeit, Python-Programme direkt aus dem Editor zu starten, z.B. Visual Studio Code (https://code.visualstudio.com/) oder geany (https://www.geany.org/).

Sinnvoll ist auch die Verwendung von thonny (https://thonny.org/), einer Python-Entwicklungsumgebung, die sich speziell an Anfänger richtet.

## Konzept

Es gibt Python-Lehrbücher, die mit der Vorstellung aller Python-Typen beginnen. In einem Anfängerkurs hat sich das für mich nicht bewährt. Daher starte ich mit dem, was die Menschen (vom Taschenrechner) sowieso schon kennen, nämlich mit Zahlen.

Ausgehend davon versuche ich, jeden Datentyp (und jede Kontrollstruktur) durch eine konkrete Problemstellung (Fallbeispiel) zu motivieren. So können erste kleinere Programme erstellte werden, bevor man beispielsweise das Konzept (und dessen Sinnhaftigkeit) eines Dictionaries verstanden haben muss.

Im Kapitel über Funktionen gehe ich kurz (am Beispiel von map / reduce) auf die funktionale Programmierung ein, um zu zeigen, dass es eine Programmierwelt neben Schleifen - die ja in Python im Zweifelsfall (zu) langsam sind - gibt.

Objektorientierung wird am Ende nur grundsätzlich eingeführt und nicht erschöpfend behandelt. Für Anfänger ist der Stoff bis dorthin schon kompliziert genug. Je nach Zeit, kann auf die Objektorientierung auch ganz verzichtet werden; es ist auch ohne Objektorientierung möglich, reale Probleme mit Python zu lösen.

Die Verwendung vorhandener (objektorientierter) Bibliotheken wird natürlich schon vorher eingeführt und motiviert.

## Verwendete Werkzeuge

Eine erste Version der Folien wurde mit einem der gängigen Präsentationsprogramme erstellt. Für einen Programmierkurs als geeigneter hat sich dann aber ein textbasiertes Format erwiesen - in dem Fall asciidoc unter Verwendung von asciidoctor-pdf.js (https://github.com/Mogztter/asciidoctor-web-pdf). 

Die Graphiken wurden mit yEd (https://www.yworks.com/products/yed) erstellt.

### Erstellung der PDF-Folien

Um die PDF-Folien aus den Asciidoc-Quellen zu erzeugen, ist zunächst asciidoctor-pdf-js zu installieren wie unter https://github.com/Mogztter/asciidoctor-web-pdf beschrieben.

Die Folien in PDF kann man dann durch einen Befehl der folgenden Art erzeugen (ausgehend vom obersten Verzeichnis, andernfalls sind die Pfade entsprechend zu anzupassen):

`asciidoctor-pdf --template-require ./Build/template.js ./FolienAsciidoc/01-einfuehrung.adoc -o ./FolienPDF/01-einfuehrung.pdf`

## Quellen

Ein solcher Kurs entsteht nicht im luftleeren Raum, sondern basiert neben eigenen Ideen und Konzepten auf verschiedenen Büchern und Kursen. Einige Referenzen seien hier beispielhaft genannt. Wo ich eine Idee oder ein Beispiel explizit übernommen habe, habe ich das in den Unterlagen entsprechend kenntlich gemacht. Sollte sich jemand trotzdem in seinen Rechten verletzt fühlen, setze er / sie sich bitte mit mir in Verbindung (s. unten).

* Bernd Klein, Einführung in Python 3, Hanser-Verlag
* Web-Seite zu diesem Buch: https://www.python-kurs.eu/
* Kofler: Python – Der Grundkurs, Rheinwerk Computing
* Johannes Ernesti, Peter Kaiser: Python 3 – Das umfassende Handbuch, Rheinwerk Computing
* Eric Matthes: Python Crashkurs – Eine praktische, projektbasierte Programmiereinführung, dpunkt.verlag
* Sweigart: Eigene Spiele programmieren: Python lernen


## Lizenz
<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Lizenzvertrag" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Pythonkurs für Programmieranfänger</span> von <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Dr. Christian Heckler</span> ist lizenziert unter einer <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Namensnennung - Nicht kommerziell - Keine Bearbeitungen 4.0 International Lizenz</a>.

Wer weitergehende Rechte möchte, wende sich gerne an mich.

## Kontakt
Fragen und Anregungen gerne an pythonkurs@ch-heckler.de.


<sup>1</sup>Im Deutschen sind hier alle Geschlechter eingeschlossen. So ist es natürlich auch in den gesamten Unterlagen zu verstehen.