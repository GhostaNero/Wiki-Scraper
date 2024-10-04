import requests
from bs4 import BeautifulSoup
import random

response = requests.get(
    url="https://en.wikipedia.org/wiki/Web_scraping",
)
soup = BeautifulSoup(response.content, "html.parser")
title = soup.find(id="firstHeading")

everyLinks = soup.find(id="bodyContent").find_all("a")
random.shuffle(everyLinks)
linkToScrape = 0

for link in everyLinks:
    
    if link['href'].find("/wiki/") == -1:
        continue
    
    
    linkToScrape = link
    break


print(linkToScrape.string)