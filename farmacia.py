from selenium import webdriver
from bs4 import BeautifulSoup



driver = webdriver.Firefox()
def vita(email):
    driver = webdriver.Firefox()
    driver.get(email[0])
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    quotes = soup.find('span', class_="priceSVG")
    rez = quotes.find('span').text
    rez_vita = f"Аптека вита: {rez} руб"
    return (rez_vita)


def mosk(email):
    driver = webdriver.Firefox()
    driver.get(email[1])
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    quotes = soup.find('div', class_='product_total_price')
    rez = quotes.find('div', class_='product_price').text
    rez_mosk = f"Аптека на Московской: {rez}"
    return (rez_mosk)


def ru(email):
    driver = webdriver.Firefox()
    driver.get(email[2])
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    quotes = soup.find('span', class_="moneyprice__content")
    rez = quotes.find('span', class_="moneyprice__roubles").text
    rez_ru = f"Аптека Ру: {rez} руб"
    return (rez_ru)





