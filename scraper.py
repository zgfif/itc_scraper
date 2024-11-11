from bs4 import BeautifulSoup
import requests

URL = 'https://itc.ua/'


def get_itc_response(url: str = URL):
    return requests.get(URL)


def get_beautiful_soup():
    return BeautifulSoup(get_itc_response().text, 'html.parser')


def get_news():
    lst  = []
    main_tag = get_beautiful_soup().main

    news = main_tag.find_all('div', class_='category-news')

    for post in news:
        dct = {} 
        dct['title'] = post.h2.text.strip()
        dct['href'] =post.h2.a['href']

        entry_header = post.find(class_='entry-header')
        dct['category'] = entry_header.div.span.text.strip()

        dct['publish_date'] = entry_header.find('span', class_='date').text.strip()
        lst.append(dct)
    
    return lst

def show_recent_news():
        news = get_news()
        for post in news:
            print(post['title'], 
                  post['href'], 
                  post['category'], 
                  post['publish_date'], 
                  sep='\n', end='\n\n')


if __name__ == '__main__':
    show_recent_news()


