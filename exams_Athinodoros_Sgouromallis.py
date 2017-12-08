import numpy
import pandas as pd
import folium
import requests
import bs4
import sklearn
import matplotlib
import dateparser
from bs4 import BeautifulSoup

url = "http://46.101.108.154/"

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

items = soup.find_all("a");
linkTexts = [item for item in items]
newFixedLinks = [];

for text in linkTexts:
    if (text.text.find("page") > -1):
        newFixedLinks.append(url+(text.text))




def scrapeSingle(url):
    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")

    all = soup.find_all('h3')
    trs = [p.parent for p in all]
    what = []
    when = []
    howM = []
    where = []
    for row in trs:  # a if condition else b
        what.append(row.find('h3').text.strip())
        when.append(row.find_all('span')[0].text.split('(')[0].strip() if "(" in row.find_all('span')[0].text else
                    row.find_all('span')[0].text.strip())
        howM.append(
            '(' + row.find_all('span')[0].text.split('(')[1].strip() if "(" in row.find_all('span')[0].text else "")
        where.append(row.find_all('span')[1].text.strip())

    data = pd.DataFrame({'What': what,
                         "When": when,
                         'How much': howM,
                         'Where': where})
    return data

frames = [scrapeSingle(url) for url in newFixedLinks]
result = pd.concat(frames)

result.to_csv('data.csv')
