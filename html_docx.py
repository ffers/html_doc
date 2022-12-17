from htmldocx import HtmlToDocx

new_parser = HtmlToDocx()
new_parser.parse_html_file("some4.html", "docx_filename")
print("Готово")
