import numpy
import pandas as pd
import folium
import requests
import bs4
import sklearn
import matplotlib
import dateparser
from bs4 import BeautifulSoup
from dateparser import parse

df = pd.read_csv("data.csv", names=['', 'How much', 'What', 'When', 'Where']);



def get_start_time(date_str):
    date_str = date_str.strip().strip('.')
    if '&' in date_str:
        date_str = date_str.split('&')[0]
    if '-' in date_str:
        date_str = date_str.split('-')[0].strip()
    if '.' in date_str:
        date_str = date_str.replace('.', ':')
    if date_str.startswith('Tues'):
        date_str = date_str.replace('Tues', 'Tue')
    if date_str.startswith('Thur'):
        date_str = date_str.replace('Thur', 'Thu')

    date = parse(date_str)
    return date


def start_time_to_float(b):
    try:
        return float("{}{:02d}".format(b.hour, b.minute))

    except:
        return numpy.math.nan



import re

def get_price(price_str):
    price_regexp = r"(?P<price>\d+)"
    if 'Free admission' in price_str:
        price = 0
    elif 'ratis' in price_str:
        price = 0
    else:
        m = re.search(price_regexp, price_str)
    try:
        price = int(m.group('price'))
    except:
        price = None
    return price
