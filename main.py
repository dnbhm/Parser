import json

import requests
from bs4 import BeautifulSoup


link="https://www.kinoafisha.info/rating/movies/"
name=requests.get(link).text
soup=BeautifulSoup(name,'lxml')
block=soup.find_all('a', class_="movieItem_title")
genre=soup.find_all('span', class_="movieItem_genres")

all_categor={}
i=0
for item in block:
    all_categor[item.text]=genre[i].text
    i+=1
print(all_categor)

with open("all_categories.json","w") as file:
    json.dump(all_categor, file, indent=4,ensure_ascii=False)

