import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv
# import cloudscraper
#
# scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
# # Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session
# print(scraper.get("https://www.myhome.ge/ka/s/").text)

url = 'https://www.myhome.ge/ka/s/?'
payloads = {'page': 1}
h = {'Accept-Language': 'en-US , ka-GE'}
file = open('myhome.ge.csv', 'w', newline='\n', encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(['ID', 'title', 'price','size','floor','rooms','beds'])


while payloads['page']<=5:
    response = requests.get(url, params=payloads, headers=h)
    print(response)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    myhome = soup.find('div', class_='statement-row-search list')
    myhome_list = myhome.find_all('div', class_='statement-card')

    for home in myhome_list:
        ID_bar = home.find('div', class_='list-view-id-container justify-content-center')
        ID=ID_bar.span.text.strip()

        card_info_bar = home.find('div', class_='card_body')

        card_name_bar=card_info_bar.find('div', class_='wrapper full-width')
        title = card_name_bar.h5.text.strip()

        price_bar=card_info_bar.find('b',class_='item-price-usd  mr-2')
        price=price_bar.text.strip()

        size_bar=card_info_bar.find('div',class_='item-size')
        size=size_bar.text.strip()

        floor_bar=card_info_bar.find('div',class_='options-texts mr-10px d-flex align-items-center stairs-hover tooltip-theme-arrows tooltip-target')
        floor=floor_bar.span.text.strip()

        room_bar=card_info_bar.find('div',class_='options-texts mr-10px d-flex align-items-center tooltip-theme-arrows tooltip-target')
        room=room_bar.span.text.strip()

        bed_bar=card_info_bar.find('div',class_='options-texts d-flex align-items-center tooltip-theme-arrows tooltip-target tooltip-element-attached-bottom tooltip-element-attached-center tooltip-target-attached-top tooltip-target-attached-center tooltip-abutted tooltip-abutted-top')
        bed=bed_bar.span.text.strip()

        print(f"{ID}\n{title}\nprice: {price}      size: {size}\nfloors: {floor}        rooms: {room}       beds: {bed}")
        csv_obj.writerow([ID,title,price,size,floor,room,bed])

    payloads['page'] += 1
    sleep(randint(15,20))


file.close()