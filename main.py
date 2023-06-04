import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv


url = f'https://armorgames.com/category/strategy-games?'
# payloads={'page':1}
payloads={'page':1}
h = {'Accept-Language': 'en-US'}
file = open('armorgames.com.csv', 'w', newline='\n', encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(['Game Name', 'Rating', 'Plays'])


# while payloads['page']<=1:
while payloads['page']<=5:
    response = requests.get(url,params=payloads, headers=h)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    product = soup.find('ul', class_='games-list')
    product_list = product.find_all('a', class_='game')


    for home in product_list:
        game_name=home.find('span',itemprop='itemListElement')
        name=game_name.div.text.strip()

        game_rating=game_name.find('td',class_='rating first')
        rating=game_rating.text.strip()

        game_plays=game_name.find('td',class_='plays')
        plays=game_plays.text.strip()

        print(f"name: {name}\nrating:{rating}       plays:{plays}\n")
        csv_obj.writerow([name, rating, plays])


    payloads['page'] += 1
    sleep(randint(15,20))


file.close()