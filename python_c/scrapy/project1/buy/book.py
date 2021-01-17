from bs4 import BeautifulSoup  
import re
import requests
import time
keyword = input('please input keyword: ')
name = input('input the author name: ')
name = name.lower()
link = f'https://search.books.com.tw/search/query/key/{keyword}/cat/all'
html = requests.get(link)
soup = BeautifulSoup(html.content,'lxml')
author_list= []
product = soup.find_all('li',class_ = 'item')

for i in product:
    try:
        for j in i.find_all('a',rel = 'go_author'):
            author_list.append(j.string.lower())
        for k in i.find_all('a',rel = 'mid_name'):
            if name in author_list or name is '':
                
                num = re.match(r".*(F\d\d\d+)/",str(k['href']))
                print(k['title'])
                print(f'https://www.books.com.tw/products/{num.group(1)}?sloc=main')
                print('price: ',i.strong.b.string)
    except:
        print('error')
    #print(author_list)

    author_list.clear()
