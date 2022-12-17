import re 

html = '<html><div><p>hello world 1</p></div><div><p>hello world 2</p></div> </html>'
re.findall(r'<p>([^<]+)</p>', html)
#['hello world 1', 'hello world 2']