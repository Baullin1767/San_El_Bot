import requests
from bs4 import BeautifulSoup

def parse_electric(url, sale=5):
    result_price:int = 0

    responce = requests.get(url)

    soup = BeautifulSoup(responce.text, "html.parser")

    prices_ = soup.find_all('div', class_='basket__p')
    names_ = soup.find_all('div', class_='basket__name js-do')
    prices = [i.text for i in prices_]
    names = [i.text for i in names_]
    for price in prices_:
        result_price += int(price.text.replace(' ','').replace('₽', ''))

    return (names, prices, int(result_price - ((result_price * sale) / 100)))