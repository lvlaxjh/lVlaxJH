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
def Dota2_hero_use_and_win():
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
    # print(all_hero_li)
    for hero in all_hero_li:
        herostr = str(hero)
        hero_name = herostr[herostr.find('hero-name-list') + 16:herostr.find('</span>')]
        hero_win = float(herostr[herostr.find('segment-green') + 28:herostr.find('%;">')])
        hero_use = herostr[herostr.find('%;"></div></td><td style="width: 30%"><div style="height: 10px">') + 64:herostr.find('segment segment-gold') - 18]
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
    # print(hero_data_dict_sort_win)
    #print(hero_data_dict_sort_use)
    #
    sort_use_list=[]
    sort_win_list=[]
    for i in hero_data_dict_sort_use:
        sort_use_list.append("H"+i+"W"+(str)(hero_data_dict_sort_use[i][0])+"U"+(str)(hero_data_dict_sort_use[i][1]))
    for i in hero_data_dict_sort_win:
        sort_win_list.append(
            "H" + i + "W" + (str)(hero_data_dict_sort_win[i][0]) + "U" + (str)(hero_data_dict_sort_win[i][1]))
    print(sort_use_list)
    print(sort_win_list)

def Dota2_hero_gpm_and_epm():
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
    url = 'http://www.dotamax.com/hero/gpm/' + url_sp['week']
    print(url)
    try:
        response = requests.get(url, headers, timeout=5)
    except TimeoutError:
        print('timeout')
    # soup: BeautifulSoup = BeautifulSoup(response.text, 'lxml')
    soup: BeautifulSoup = BeautifulSoup(response.text,'html.parser')
    hero_data_dict = {}
    all_hero_li = soup.find_all('tr')
    print(all_hero_li)
    for hero in all_hero_li:
        herostr = str(hero)
        hero_name = herostr[herostr.find('hero-name-list') + 16:herostr.find('</span>')]
        hero_gpm = float(herostr[herostr.find('</td><td style="width: 30%"><div style="height: 10px">') + 54:herostr.find('</div><div class="segment segment-gold"')])
        hero_epm = herostr[herostr.find('</td><td style="width: 40%"><div style="height: 10px">') + 54:herostr.find('</div><div class="segment segment-green"')]
        # hero_use = int(hero_use.replace(',', ''))
        print(hero_name)
        print(hero_gpm)
        print(hero_epm)
    #     hero_data_dict[hero_name] = [hero_win, hero_use]
    # hero_data_dict_sort_win = {}
    # hero_data_dict_sort_use = {}
    # hero_data_list_sort_win = sorted(hero_data_dict.items(), key=lambda x: x[1][0])
    # hero_data_list_sort_use = sorted(hero_data_dict.items(), key=lambda x: x[1][1])
    # for i in hero_data_list_sort_win:
    #     hero_data_dict_sort_win[i[0]] = [i[1][0], i[1][1]]
    # for i in hero_data_list_sort_use:
    #     hero_data_dict_sort_use[i[0]] = [i[1][0], i[1][1]]
    # # print(hero_data_dict_sort_win)
    # #print(hero_data_dict_sort_use)
    # #
    # sort_use_list=[]
    # sort_win_list=[]
    # for i in hero_data_dict_sort_use:
    #     sort_use_list.append("H"+i+"W"+(str)(hero_data_dict_sort_use[i][0])+"U"+(str)(hero_data_dict_sort_use[i][1]))
    # for i in hero_data_dict_sort_win:
    #     sort_win_list.append(
    #         "H" + i + "W" + (str)(hero_data_dict_sort_win[i][0]) + "U" + (str)(hero_data_dict_sort_win[i][1]))
    # print(sort_use_list)
    # print(sort_win_list)

if __name__ == "__main__":
    Dota2_hero_gpm_and_epm()
