from bs4 import BeautifulSoup
import json

f = open('some4.html', 'r')
soup = BeautifulSoup(f, features='lxml')
divs = soup.find_all('div', 'title')
with open('txt/input.txt', 'w', encoding='utf-8') as fw:
	for div in divs:
	    ps = div.find_all('p')
	    for p in ps:
	    	fw.write(p.get_text())
print('Успех')

'''

Вся ваша проблема состоит в том, что Вы хотите получить текст со всех тегов 'p', но при этом вы извлекаете лишь один тег 'div'
Если Вы хотите получить текст из всех тегов 'p', то Вам надо для начала прочитать все теги 'div'.
tags = soup.find('div')
Стоит заменить на:

tags = soup.find_all('div')

Благодаря этому мы получаем массив, в котором лежат все наши теги 'div'
Посмотрим на наш текущий массив, который хранит переменная tags:

[<div><p>hello world 1</p></div>, <div><p>hello world 2</p></div>]


#После чего его следует перебрать

for x in tags:
#Перебирая элементы массива с тегами 'div', нам надо получать новый массив, который будет содержать элементы с тегами 'p', которые расположены в определенном теге 'div'

for x in tags:
    texts = x.find_all('p')


#Теперь у нас есть массив тегов 'p' в определенном 'div' ( находится в переменной texts ), который генерируется с разными элементами для определенного тега 'div' при переборе массива tags, осталось лишь перебрать этот массив и получить текст с каждого тега 'p'

for text in texts:
    print(text.get_text())


#Полный код ( переименовал переменные для большей читаемости )

soup = BeautifulSoup('<html><div><p>hello world 1</p></div><div><p>hello world 2</p></div></html>', features='lxml')
divs = soup.find_all('div')
for div in divs:
    ps = div.find_all('p')
    for p in ps:
        print(p.get_text())
'''