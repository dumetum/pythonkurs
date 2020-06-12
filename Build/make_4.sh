rm ../FolienPDF/04-funktionen.pdf
rm ../FolienAsciidoc/04-funktionen.html
asciidoctor-pdf --template-require ./../Build/template.js ../FolienAsciidoc/04-funktionen.adoc -o ../FolienPDF/04-funktionen.pdf
rm ../FolienAsciidoc/04-funktionen.html
