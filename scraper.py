from bs4 import BeautifulSoup
import requests

URL = 'https://itc.ua/'

response = requests.get(URL)
bs = BeautifulSoup(response.text, 'html.parser')

main = bs.main

news = main.find_all('div', class_='category-news')

for post in news:
    print('title: ', post.h2.text.strip())
    print('href: ', post.h2.a['href'])
    entry_header = post.find(class_='entry-header')
    print('category:', entry_header.div.span.text.strip())

    print('Date: ', entry_header.find('span', class_='date').text.strip())
    print('')

