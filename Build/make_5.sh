rm ../FolienPDF/05-AusnahmenModuleDateien.pdf
rm ../FolienAsciidoc/05-AusnahmenModuleDateien.html
asciidoctor-pdf --template-require ./../Build/template.js ../FolienAsciidoc/05-AusnahmenModuleDateien.adoc -o ../FolienPDF/05-AusnahmenModuleDateien.pdf
rm ../FolienAsciidoc/05-AusnahmenModuleDateien.html
