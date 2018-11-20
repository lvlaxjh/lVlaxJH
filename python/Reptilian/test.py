# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

####
# def Dict_Sort(_Dict={}):
#     list=sorted(_Dict,key=lambda x:_Dict[x])
# def Dict_Sort(_Dict={},_int=0):
#     list=sorted(_Dict,key=lambda x:_Dict[x][_int])
#     sort_dict=map(lambda x:{x:_Dict[x]}, list)
#     return  sort_dict
def Dota2_hero_data():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    url = 'https://music.163.com/#/song?id=1303019637'
    print(url)
    response = requests.get(url, headers, timeout=5)
    soup = BeautifulSoup(response.text)
    print(soup.prettify())
if __name__ == "__main__":
    Dota2_hero_data()
