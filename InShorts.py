from bs4 import BeautifulSoup as beauty
from textblob import TextBlob
import requests

source = requests.get('https://inshorts.com/en/read').text
soup = beauty(source,'lxml')

for news in soup.find_all('div',class_='news-card z-depth-1'):
    news_headline = news.find('div',class_='news-card-title news-right-box')
    news_headline = news_headline.a.span.text
    trans_headline = TextBlob(news_headline)
    print(trans_headline.translate(to='hi'))

    news_content = news.find('div',class_='news-card-content news-right-box')
    news_content = news_content.div.text
    trans_content = TextBlob(news_content)
    print(trans_content.translate(to='hi'))
    
    print()
