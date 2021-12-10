import requests
from bs4 import BeautifulSoup
import os
import json

url = 'https://www.detik.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.93 Safari/537.36 '
}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')


def get_news_popular():
    popular = soup.find('div', 'box cb-mostpop')
    article = popular.find_all('article', 'list-content__item')
    popular_news = []
    for item in article:
        title = item.find('a')['dtr-ttl']
        link = item.find('a')['href']
        time = item.find('div', 'media__date')
        date = time.find('span')['title']
        result = {
            'title': title,
            'link': link,
            'date': date
        }
        popular_news.append(result)

    try:
        os.mkdir('json_result')
    except FileExistsError:
        pass

    with open('json_result/popular_news.json', 'w+') as json_data:
        json.dump(popular_news, json_data)
    print('json created')


if __name__ == '__main__':
    get_news_popular()