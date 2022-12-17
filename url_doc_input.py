#неплохо создать бы input из консоли 

#можно использовать sys для ввода информации
#python convert_pdf2docx.py letter.pdf letter.docx
"""
if __name__ == "__main__":
    import sys
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_pdf2docx(input_file, output_file)
"""
#скачать страницу:

import urllib
import requests
from bs4 import BeautifulSoup

url_download = input()
#"https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models"
def parse_html():
    resp=requests.get(url_download)
    html = resp.text
    soup = BeautifulSoup(html, "lxml")
    f = open('some4.html', 'w')
    f.write(soup.prettify())
    f.close()
    print("Страница скачана!")
    create_docx()


#Создать docx:
from htmldocx import HtmlToDocx

def create_docx():
    new_parser = HtmlToDocx()
    new_parser.parse_html_file("some4.html", "docx_filename") 
    '''
    Тут можно сделать генерацию имени файла от даты или урла
    '''
    print("Docx создан!")
   

parse_html()

