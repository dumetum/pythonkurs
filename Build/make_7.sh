rm ../FolienPDF/07-Ableitung.pdf
rm ../FolienAsciidoc/07-Ableitung.html
asciidoctor-pdf --template-require ./../Build/template.js ../FolienAsciidoc/07-Ableitung.adoc -o ../FolienPDF/07-Ableitung.pdf
rm ../FolienAsciidoc/07-Ableitung.html
