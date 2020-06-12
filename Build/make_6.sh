rm ../FolienPDF/06-oop.pdf
rm ../FolienAsciidoc/06-oop.html
asciidoctor-pdf --template-require ./../Build/template.js ../FolienAsciidoc/06-oop.adoc -o ../FolienPDF/06-oop.pdf
rm ../FolienAsciidoc/06-oop.html
