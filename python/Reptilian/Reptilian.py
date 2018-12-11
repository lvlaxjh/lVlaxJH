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
    soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
    hero_data_dict = {}
    all_hero_li = soup.find_all('tr')
    # print(all_hero_li)
    for hero in all_hero_li:
        herostr = str(hero)
        hero_name = herostr[herostr.find('hero-name-list') + 16:herostr.find('</span>')]
        hero_win = float(herostr[herostr.find('segment-green') + 28:herostr.find('%;">')])
        hero_use = herostr[
                   herostr.find('%;"></div></td><td style="width: 30%"><div style="height: 10px">') + 64:herostr.find(
                       'segment segment-gold') - 18]
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
    # print(hero_data_dict_sort_use)
    #
    sort_use_list = []
    sort_win_list = []
    for i in hero_data_dict_sort_use:
        sort_use_list.append(
            "H" + i + "W" + (str)(hero_data_dict_sort_use[i][0]) + "U" + (str)(hero_data_dict_sort_use[i][1]))
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
    soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
    hero_data_dict = {}
    all_hero_li = soup.find_all('tr')
    # print(all_hero_li)
    for hero in all_hero_li:
        herostr = str(hero)
        hero_name = herostr[herostr.find('hero-name-list') + 16:herostr.find('</span>')]
        hero_gpm = float(herostr[
                         herostr.find('</td><td style="width: 30%"><div style="height: 10px">') + 54:herostr.find(
                             '</div><div class="segment segment-gold"')])
        hero_epm = herostr[herostr.find('</td><td style="width: 40%"><div style="height: 10px">') + 54:herostr.find(
            '</div><div class="segment segment-green"')]
        # print(hero_name)
        # print(hero_gpm)
        # print(hero_epm)
        hero_data_dict[hero_name] = [hero_gpm, hero_epm]
    hero_data_dict_sort_gpm = {}
    hero_data_dict_sort_epm = {}
    hero_data_list_sort_gpm = sorted(hero_data_dict.items(), key=lambda x: x[1][0])
    hero_data_list_sort_epm = sorted(hero_data_dict.items(), key=lambda x: x[1][1])
    for i in hero_data_list_sort_gpm:
        hero_data_dict_sort_gpm[i[0]] = [i[1][0], i[1][1]]
    for i in hero_data_list_sort_epm:
        hero_data_dict_sort_epm[i[0]] = [i[1][0], i[1][1]]
    # print(hero_data_dict_sort_gpm)
    # print(hero_data_dict_sort_epm)
    sort_gpm_list = []
    sort_epm_list = []
    for i in hero_data_dict_sort_gpm:
        sort_gpm_list.append(
            "H" + i + "G" + (str)(hero_data_dict_sort_gpm[i][0]) + "E" + (str)(hero_data_dict_sort_gpm[i][1]))
    for i in hero_data_dict_sort_epm:
        sort_epm_list.append(
            "H" + i + "G" + (str)(hero_data_dict_sort_epm[i][0]) + "E" + (str)(hero_data_dict_sort_epm[i][1]))
    print(sort_gpm_list)
    print(sort_epm_list)


def Dota2_hero_KDA():
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
    url = 'http://www.dotamax.com/hero/kda/' + url_sp['week']
    print(url)
    try:
        response = requests.get(url, headers, timeout=5)
    except TimeoutError:
        print('timeout')
    # soup: BeautifulSoup = BeautifulSoup(response.text, 'lxml')
    soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
    hero_data_dict = {}
    all_hero_li = soup.find_all('tr')
    # print(all_hero_li)
    for hero in all_hero_li:
        herostr = str(hero)
        hero_name = herostr[herostr.find('hero-name-list') + 16:herostr.find('</span>')]
        hero_kda = float(herostr[
                         herostr.find('</td><td style="width: 25%"><div style="height: 10px">') + 54:herostr.find(
                             '</div><div class="segment segment-gold"')])

        herostr = herostr[herostr.find('</td><td style="width: 25%"><div style="height: 10px">') + 54:]
        hero_k = float(herostr[
                       herostr.find('</td><td style="width: 16.5%"><div style="height: 10px">') + 56:herostr.find(
                           '</div><div class="segment segment-red"')])
        herostr = herostr[herostr.find('</td><td style="width: 16.5%"><div style="height: 10px">') + 56:]
        hero_d = float(herostr[
                       herostr.find('</td><td style="width: 16.5%"><div style="height: 10px">') + 56:herostr.find(
                           '</div><div class="segment segment-gray"')])
        herostr = herostr[herostr.find('</td><td style="width: 16.5%"><div style="height: 10px">') + 56:]
        hero_a = float(herostr[
                       herostr.find('</td><td style="width: 16.5%"><div style="height: 10px">') + 56:herostr.find(
                           '</div><div class="segment segment-green"')])
        # print(hero_name)
        # print(hero_kda)
        # print(hero_k)
        # print(hero_d)
        # print(hero_a)
        hero_data_dict[hero_name] = [hero_kda, hero_k, hero_d, hero_a]
    hero_data_dict_sort_kda = {}
    hero_data_dict_sort_k = {}
    hero_data_dict_sort_d = {}
    hero_data_dict_sort_a = {}
    hero_data_list_sort_kda = sorted(hero_data_dict.items(), key=lambda x: x[1][0])
    hero_data_list_sort_k = sorted(hero_data_dict.items(), key=lambda x: x[1][1])
    hero_data_list_sort_d = sorted(hero_data_dict.items(), key=lambda x: x[1][2])
    hero_data_list_sort_a = sorted(hero_data_dict.items(), key=lambda x: x[1][3])
    for i in hero_data_list_sort_kda:
        hero_data_dict_sort_kda[i[0]] = [i[1][0], i[1][1], i[1][2], i[1][3]]
    for i in hero_data_list_sort_k:
        hero_data_dict_sort_k[i[0]] = [i[1][0], i[1][1], i[1][2], i[1][3]]
    for i in hero_data_list_sort_d:
        hero_data_dict_sort_d[i[0]] = [i[1][0], i[1][1], i[1][2], i[1][3]]
    for i in hero_data_list_sort_a:
        hero_data_dict_sort_a[i[0]] = [i[1][0], i[1][1], i[1][2], i[1][3]]
    # # print(hero_data_dict_sort_gpm)
    # # print(hero_data_dict_sort_epm)
    sort_kda_list = []
    sort_k_list = []
    sort_d_list = []
    sort_a_list = []
    for i in hero_data_dict_sort_kda:
        sort_kda_list.append("H" + i + "KDA" + (str)(hero_data_dict_sort_kda[i][0]) + "K" + (str)(
            hero_data_dict_sort_kda[i][1]) + "D" + (str)(hero_data_dict_sort_kda[i][2]) + "A" + (str)(
            hero_data_dict_sort_kda[i][3]))
    for i in hero_data_dict_sort_k:
        sort_k_list.append("H" + i + "KDA" + (str)(hero_data_dict_sort_k[i][0]) + "K" + (str)(
            hero_data_dict_sort_k[i][1]) + "D" + (str)(hero_data_dict_sort_k[i][2]) + "A" + (str)(
            hero_data_dict_sort_k[i][3]))
    for i in hero_data_dict_sort_d:
        sort_d_list.append("H" + i + "KDA" + (str)(hero_data_dict_sort_d[i][0]) + "K" + (str)(
            hero_data_dict_sort_d[i][1]) + "D" + (str)(hero_data_dict_sort_d[i][2]) + "A" + (str)(
            hero_data_dict_sort_d[i][3]))
    for i in hero_data_dict_sort_a:
        sort_a_list.append("H" + i + "KDA" + (str)(hero_data_dict_sort_a[i][0]) + "K" + (str)(
            hero_data_dict_sort_a[i][1]) + "D" + (str)(hero_data_dict_sort_a[i][2]) + "A" + (str)(
            hero_data_dict_sort_a[i][3]))
    # for i in hero_data_dict_sort_epm:
    #     sort_epm_list.append(
    #         "H" + i + "G" + (str)(hero_data_dict_sort_epm[i][0]) + "E" + (str)(hero_data_dict_sort_epm[i][1]))
    print(sort_kda_list)
    print(sort_k_list)
    print(sort_d_list)
    print(sort_a_list)


def Dota2_hero_dmg_and_treat_arc():
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
    url = 'http://www.dotamax.com/hero/dmg/' + url_sp['week']
    print(url)
    try:
        response = requests.get(url, headers, timeout=5)
    except TimeoutError:
        print('timeout')
    # soup: BeautifulSoup = BeautifulSoup(response.text, 'lxml')
    soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
    hero_data_dict = {}
    all_hero_li = soup.find_all('tr')
    # print(all_hero_li)
    for hero in all_hero_li:
        herostr = str(hero)
        hero_name = herostr[herostr.find('hero-name-list') + 16:herostr.find('</span>')]
        hero_dmg = float(herostr[
                         herostr.find('</td><td style="width: 25%"><div style="height: 10px">') + 54:herostr.find(
                             '</div><div class="segment segment-red"')])
        herostr = herostr[herostr.find('</td><td style="width: 25%"><div style="height: 10px">') + 54:]
        hero_treat = float(herostr[
                         herostr.find('</td><td style="width: 25%"><div style="height: 10px">') + 54:herostr.find(
            '</div><div class="segment segment-green"')])
        herostr = herostr[herostr.find('</td><td style="width: 25%"><div style="height: 10px">') + 54:]
        hero_arc = float(herostr[
                         herostr.find('</td><td style="width: 25%"><div style="height: 10px">') + 54:herostr.find(
            '</div><div class="segment segment-white"')])
        # print(hero_name)
        # print(hero_dmg)
        # print(hero_treat)
        hero_data_dict[hero_name] = [hero_dmg, hero_treat, hero_arc]
    hero_data_dict_sort_dmg = {}
    hero_data_dict_sort_treat = {}
    hero_data_dict_sort_arc = {}
    hero_data_list_sort_dmg = sorted(hero_data_dict.items(), key=lambda x: x[1][0])
    hero_data_list_sort_treat = sorted(hero_data_dict.items(), key=lambda x: x[1][1])
    hero_data_list_sort_arc = sorted(hero_data_dict.items(), key=lambda x: x[1][2])
    for i in hero_data_list_sort_dmg:
        hero_data_dict_sort_dmg[i[0]] = [i[1][0], i[1][1], i[1][2]]
    for i in hero_data_list_sort_treat:
        hero_data_dict_sort_treat[i[0]] = [i[1][0], i[1][1], i[1][2]]
    for i in hero_data_list_sort_arc:
        hero_data_dict_sort_arc[i[0]] = [i[1][0], i[1][1], i[1][2]]
    # # print(hero_data_dict_sort_gpm)
    # # print(hero_data_dict_sort_epm)
    sort_dmg_list = []
    sort_treat_list = []
    sort_arc_list = []
    for i in hero_data_dict_sort_dmg:
        sort_dmg_list.append(
            "H" + i + "D" + (str)(hero_data_dict_sort_dmg[i][0]) + "T" + (str)(hero_data_dict_sort_dmg[i][1]) + "A" + (
                str)(hero_data_dict_sort_dmg[i][2]))
    for i in hero_data_dict_sort_treat:
        sort_treat_list.append(
            "H" + i + "D" + (str)(hero_data_dict_sort_treat[i][0]) + "T" + (str)(
                hero_data_dict_sort_treat[i][1]) + "A" + (str)(hero_data_dict_sort_treat[i][2]))
    for i in hero_data_dict_sort_arc:
        sort_arc_list.append(
            "H" + i + "D" + (str)(hero_data_dict_sort_arc[i][0]) + "T" + (str)(hero_data_dict_sort_arc[i][1]) + "A" + (
                str)(hero_data_dict_sort_arc[i][2]))
    print(sort_dmg_list)
    print(sort_treat_list)
    print(sort_arc_list)


if __name__ == "__main__":
    Dota2_hero_dmg_and_treat_arc()
