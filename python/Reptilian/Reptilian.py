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
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 47.0.2526.106BIDUBrowser / 8.7Safari / 537.36'
    }
    url_sp = {
        ###
        'alltime': '?time=all',  # 全部
        'month': '?time=month',  # 本月
        'week': '?time=week',  # 本周
        ###
        'allser': '&server=all',  # 全球
        'world': '&server=world',  # 国外
        'china': '&server=cn',  # 中国
        ###
        'n': '&skill=n',  # n局
        'h': '&skill=h',  # h局
        'vh': '&skill=vh',  # vh局
        'pro': '&skill=pro',  # 职业
        'all': '&skill=all',  # 全部
        ###
        'allmatch': '&ladder=all',  # 全部比赛
        'y': '&ladder=y',  # 天梯比赛
        'nmatch': '&ladder=n',  # 普通比赛
        'solo': '&ladder=solo'  # solo
        ###
    }
    url = 'http://www.dotamax.com/hero/rate/' + url_sp['week']
    print(url)
    try:
        response = requests.get(url, headers, timeout=5)
    except TimeoutError:
        print('timeout')
    # soup: BeautifulSoup = BeautifulSoup(response.text, 'lxml')
    soup: BeautifulSoup = BeautifulSoup(response.text,'html.parser')
    hero_data_dict = {}
    all_hero_li = soup.find_all('tr')
    for hero in all_hero_li:
        herostr = str(hero)
        hero_name = herostr[herostr.find('hero-name-list') + 16:herostr.find('</span>')]
        hero_win = float(herostr[herostr.find('segment segment-green') + 36:herostr.find('%;">')])
        hero_use = herostr[herostr.find('segment segment-green') + 113:herostr.find('segment segment-gold') - 18]
        hero_use = int(hero_use.replace(',', ''))
        # print(hero_name)
        # print(hero_win)
        # print(hero_use)
        hero_data_dict[hero_name] = [hero_win, hero_use]
    hero_data_dict_sort_win = {}
    hero_data_dict_sort_use = {}
    hero_data_list_sort_win = sorted(hero_data_dict.items(), key=lambda x: x[1][0])
    hero_data_list_sort_use = sorted(hero_data_dict.items(), key=lambda x: x[1][1])
    for i in hero_data_list_sort_win:
        hero_data_dict_sort_win[i[0]] = [i[1][0], i[1][1]]
    for i in hero_data_list_sort_use:
        hero_data_dict_sort_use[i[0]] = [i[1][0], i[1][1]]
    print(hero_data_dict_sort_win)
    print(hero_data_dict_sort_use)
    # print(str_i[str_i.Find(r'\''):str_i.find(',')-1])
    # print(hero_data_dict_sort_win)


if __name__ == "__main__":
    Dota2_hero_data()
