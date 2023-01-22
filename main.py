import requests as req
from bs4 import BeautifulSoup
from fake_useragent import FakeUserAgent

url = 'https://www.binance.com/ru/markets'

user_agent = FakeUserAgent().random()
headers = {
    'user_agent': user_agent
}

response = req.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
data = soup.find_all('div', class_='css-leyy1t')


for card in data:

    currency = card.find('div', class_='css-y492if').text
    price = card.find('div', class_='css-ydcgk2').text
    capitalization = card.find('div', class_='css-s779xv').text

    print(f'{currency}  {price}  {capitalization}')
