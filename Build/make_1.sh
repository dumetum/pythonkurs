rm ../FolienPDF/01-einfuehrung.pdf
rm ../FolienAsciidoc/01-einfuehrung.html
asciidoctor-pdf --template-require ./../Build/template.js ../FolienAsciidoc/01-einfuehrung.adoc -o ../FolienPDF/01-einfuehrung.pdf
rm ../FolienAsciidoc/01-einfuehrung.html
