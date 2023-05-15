import csv
import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://www.amazon.com/s?k=smartphones&crid=3MRTHW3UCOCAY&sprefix=smartphones%2Caps%2C163&ref=nb_sb_noss_1"

headers = {
    "Accept-Language": "es-ES,es;q=0.9,de-DE;q=0.8,de;q=0.7,gl-ES;q=0.6,gl;q=0.5,en-GB;q=0.4,en;q=0.3",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=headers)
website = response.text
soup = BeautifulSoup(website, "lxml")

names = soup.find_all(name="span", class_="a-text-normal")
smartphones = [name.text for name in names]
links = soup.find_all(name="a", class_="a-text-normal")
link_list = [link['href'] for link in links]
for i in range(len(link_list)):
    link_list[i] = "https://www.amazon.com" + link_list[i]
qualif = soup.find_all(name="span", class_="a-icon-alt")
stars = [star.text for star in qualif]
dollars = soup.find_all(name="span", class_="a-offscreen")
prices = [price.text for price in dollars]

search_list=[]
search_list.append(smartphones)
search_list.append(stars)
search_list.append(prices)
search_list.append(link_list)

with open("smartphone_search_list.csv", "w") as file:
    output = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=";")
    output.writerows(zip(smartphones, stars, prices, link_list))


