from bs4 import BeautifulSoup  
import re
import requests
q = input('search: ')
link = f'https://www.ptt.cc/bbs/NTHU_Course/search?q={q}'
html = requests.get(link)
soup = BeautifulSoup(html.content,'lxml')

for i in soup.find_all('a',href=re.compile('.*A.[0-9A-Z]+.html')):
    print(i.string)
    link_2 = 'https://www.ptt.cc'+ i['href']
    print(link_2)