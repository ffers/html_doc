from urllib.request import urlopen
import html5lib

with urlopen("https://www.google.ru/") as f:
    document = html5lib.parse(f, transport_encoding=f.info().get_content_charset())
    f = open('some.html', 'w')
    f.write(document)
    f.close()