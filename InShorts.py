from bs4 import BeautifulSoup as beauty
import requests

source = requests.get('https://inshorts.com/en/read').text
soup = beauty(source,'lxml')

for news in soup.find_all('div',class_='news-card z-depth-1'):
    news_headline = news.find('div',class_='news-card-title news-right-box')
    news_headline = news_headline.a.span.text
    print(news_headline)

    news_content = news.find('div',class_='news-card-content news-right-box')
    news_content = news_content.div.text
    print(news_content)

    print()


