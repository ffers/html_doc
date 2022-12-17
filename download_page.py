import urllib
import requests
from bs4 import BeautifulSoup

url = input()
resp = requests.get(url)
html = resp.text
soup = BeautifulSoup(html, "html.parser")
f = open('some4.html', 'w', encoding='utf-8')
f.write(soup.prettify())
f.close()

tags = soup.find_all('main')
print(tags)
with open('txt/tags.txt', 'w', encoding='utf-8') as fw:
	for main in tags:
		fw.write(tags.get_text("\n"))
"""	    ps = tags.find_all('p')
		for p in ps:
			fw.write(p.get_text("\n"))"""


print("Успех!")
