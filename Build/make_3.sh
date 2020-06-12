rm ../FolienPDF/03-schleifen.pdf
rm ../FolienAsciidoc/03-schleifen.html
asciidoctor-pdf --template-require ./../Build/template.js ../FolienAsciidoc/03-schleifen.adoc -o ../FolienPDF/03-schleifen.pdf
rm ../FolienAsciidoc/03-schleifen.html
