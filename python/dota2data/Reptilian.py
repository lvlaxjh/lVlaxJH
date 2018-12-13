# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import datetime
import pymysql


# {'****':[win,use,gpm,epm,kda,k,d,a,dmg,treat,arc]}

####
# def Dict_Sort(_Dict={}):
#     list=sorted(_Dict,key=lambda x:_Dict[x])
# def Dict_Sort(_Dict={},_int=0):
#     list=sorted(_Dict,key=lambda x:_Dict[x][_int])
#     sort_dict=map(lambda x:{x:_Dict[x]}, list)
#     return  sort_dict
def Dota2_hero_use_and_win(types):
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 47.0.2526.106BIDUBrowser / 8.7Safari / 537.36'
    }

    url = 'http://www.dotamax.com/hero/rate/' + '?time=week' + types
    print(url)
    try:
        response = requests.get(url, headers, timeout=5)
    except TimeoutError:
        print('timeout')
    # soup: BeautifulSoup = BeautifulSoup(response.text, 'lxml')
    soup= BeautifulSoup(response.text, 'html.parser')
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
    return hero_data_dict


def Dota2_hero_gpm_and_epm(types):
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 47.0.2526.106BIDUBrowser / 8.7Safari / 537.36'
    }
    url = 'http://www.dotamax.com/hero/gpm/' + '?time=week' + types
    print(url)
    try:
        response = requests.get(url, headers, timeout=5)
    except TimeoutError:
        print('timeout')
    # soup: BeautifulSoup = BeautifulSoup(response.text, 'lxml')
    soup= BeautifulSoup(response.text, 'html.parser')
    hero_data_dict = {}
    all_hero_li = soup.find_all('tr')
    # print(all_hero_li)
    for hero in all_hero_li:
        herostr = str(hero)
        hero_name = herostr[herostr.find('hero-name-list') + 16:herostr.find('</span>')]
        hero_gpm = float(herostr[
                         herostr.find('</td><td style="width: 30%"><div style="height: 10px">') + 54:herostr.find(
                             '</div><div class="segment segment-gold"')])
        hero_epm = float(herostr[
                         herostr.find('</td><td style="width: 40%"><div style="height: 10px">') + 54:herostr.find(
                             '</div><div class="segment segment-green"')])
        # print(hero_name)
        # print(hero_gpm)
        # print(hero_epm)
        hero_data_dict[hero_name] = [hero_gpm, hero_epm]

    return hero_data_dict


def Dota2_hero_KDA(types):
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 47.0.2526.106BIDUBrowser / 8.7Safari / 537.36'
    }
    url = 'http://www.dotamax.com/hero/kda/' + '?time=week' + types
    print(url)
    try:
        response = requests.get(url, headers, timeout=5)
    except TimeoutError:
        print('timeout')
    # soup: BeautifulSoup = BeautifulSoup(response.text, 'lxml')
    soup = BeautifulSoup(response.text, 'html.parser')
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

    return hero_data_dict


def Dota2_hero_dmg_and_treat_arc(types):
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 47.0.2526.106BIDUBrowser / 8.7Safari / 537.36'
    }
    url = 'http://www.dotamax.com/hero/dmg/' + '?time=week' + types
    print(url)
    try:
        response = requests.get(url, headers, timeout=5)
    except TimeoutError:
        print('timeout')
    # soup: BeautifulSoup = BeautifulSoup(response.text, 'lxml')
    soup = BeautifulSoup(response.text, 'html.parser')
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
    return hero_data_dict


def all_hero_data(types):

    hero_name_win_use = {}
    hero_gpm_epm = {}
    hero_kda = {}
    hero_dmg_treat_arc = {}
    hero_name_win_use = Dota2_hero_use_and_win(types)
    hero_gpm_epm = Dota2_hero_gpm_and_epm(types)
    hero_kda = Dota2_hero_KDA(types)
    hero_dmg_treat_arc = Dota2_hero_dmg_and_treat_arc(types)
    for i in hero_name_win_use:
        for n in hero_gpm_epm:
            if i == n:
                hero_name_win_use[i].append(hero_gpm_epm[n][0])
                hero_name_win_use[i].append(hero_gpm_epm[n][1])

    for i in hero_name_win_use:
        for n in hero_kda:
            if i == n:
                hero_name_win_use[i].append(hero_kda[n][0])
                hero_name_win_use[i].append(hero_kda[n][1])
                hero_name_win_use[i].append(hero_kda[n][2])
                hero_name_win_use[i].append(hero_kda[n][3])
    for i in hero_name_win_use:
        for n in hero_dmg_treat_arc:
            if i == n:
                hero_name_win_use[i].append(hero_dmg_treat_arc[n][0])
                hero_name_win_use[i].append(hero_dmg_treat_arc[n][1])
                hero_name_win_use[i].append(hero_dmg_treat_arc[n][2])
    all_hero_datas = {}
    all_hero_datas = hero_name_win_use
    times = datetime.datetime.now().strftime('%Y-%m-%d')
    for i in all_hero_datas:
        all_hero_datas[i].append(types)
    for i in all_hero_datas:
        all_hero_datas[i].append(times)
    return all_hero_datas
    # sort_win = []
    # sort_use = []
    # sort_gpm = []
    # sort_epm = []
    # sort_kda = []
    # sort_k = []
    # sort_d = []
    # sort_a = []
    # sort_dmg = []
    # sort_treat = []
    # sort_arc = []
    # sort_win = sorted(all_hero_datas.items(), key=lambda x: x[1][0])
    # sort_use = sorted(all_hero_datas.items(), key=lambda x: x[1][1])
    # sort_gpm = sorted(all_hero_datas.items(), key=lambda x: x[1][2])
    # sort_epm = sorted(all_hero_datas.items(), key=lambda x: x[1][3])
    # sort_kda = sorted(all_hero_datas.items(), key=lambda x: x[1][4])
    # sort_k = sorted(all_hero_datas.items(), key=lambda x: x[1][5])
    # sort_d = sorted(all_hero_datas.items(), key=lambda x: x[1][6])
    # sort_a = sorted(all_hero_datas.items(), key=lambda x: x[1][7])
    # sort_dmg = sorted(all_hero_datas.items(), key=lambda x: x[1][8])
    # sort_treat = sorted(all_hero_datas.items(), key=lambda x: x[1][9])
    # sort_arc = sorted(all_hero_datas.items(), key=lambda x: x[1][10])
    # print(sort_win,sort_use,sort_gpm,sort_epm,sort_kda,sort_k,sort_d,sort_a,sort_dmg,sort_treat,sort_arc)
    # {'****':[win,use,gpm,epm,kda,k,d,a,dmg,treat,arc]}
    # print(hero_name_win_use)
    # print(hero_gpm_epm)
    # print(hero_kda)
    # print(hero_dmg_treat_arc)


def input_mysql_all(types):
    db = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='jhczxcvbnm',
        db='dota2data',
        charset='utf8'
    )
    #
    datas = {}
    datas = all_hero_data(types)
    #
    # for a in datas['敌法师']:
    #     print(type(a))

    for i in datas:
        cursor = db.cursor()
        sql = '''insert into dota2dataall(heroname,allwin,alluse,gpm,epm,kda,k,d,a,dmg,treat,arc,state,times)\
        values ("%s","%f","%d","%f","%f","%f","%f","%f","%f","%f","%f","%f","%s","%s")''' % (
            i, datas[i][0], datas[i][1], datas[i][2], datas[i][3], datas[i][4], datas[i][5], datas[i][6], datas[i][7],datas[i][8], datas[i][9], datas[i][10], datas[i][11], datas[i][12])
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            db.commit()
        except:
            # 发生错误时回滚
            print('error')
            db.rollback()

    db.close()
def input_mysql_pro(types):
    db = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='jhczxcvbnm',
        db='dota2data',
        charset='utf8'
    )
    #
    datas = {}
    datas = all_hero_data(types)
    #
    # for a in datas['敌法师']:
    #     print(type(a))

    for i in datas:
        cursor = db.cursor()
        sql = '''insert into dota2datapro(heroname,allwin,alluse,gpm,epm,kda,k,d,a,dmg,treat,arc,state,times)\
        values ("%s","%f","%d","%f","%f","%f","%f","%f","%f","%f","%f","%f","%s","%s")''' % (
            i, datas[i][0], datas[i][1], datas[i][2], datas[i][3], datas[i][4], datas[i][5], datas[i][6], datas[i][7],datas[i][8], datas[i][9], datas[i][10], datas[i][11], datas[i][12])
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            db.commit()
        except:
            # 发生错误时回滚
            print('error')
            db.rollback()

    db.close()
def input_mysql_vh(types):
    db = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='jhczxcvbnm',
        db='dota2data',
        charset='utf8'
    )
    #
    datas = {}
    datas = all_hero_data(types)
    #
    # for a in datas['敌法师']:
    #     print(type(a))

    for i in datas:
        cursor = db.cursor()
        sql = '''insert into dota2datavh(heroname,allwin,alluse,gpm,epm,kda,k,d,a,dmg,treat,arc,state,times)\
        values ("%s","%f","%d","%f","%f","%f","%f","%f","%f","%f","%f","%f","%s","%s")''' % (
            i, datas[i][0], datas[i][1], datas[i][2], datas[i][3], datas[i][4], datas[i][5], datas[i][6], datas[i][7],datas[i][8], datas[i][9], datas[i][10], datas[i][11], datas[i][12])
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            db.commit()
        except:
            # 发生错误时回滚
            print('error')
            db.rollback()

    db.close()

if __name__ == "__main__":
    # all_hero_data()
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
    input_mysql_all(url_sp['allser']+url_sp['all']+url_sp['allmatch'])
    input_mysql_pro(url_sp['allser']+url_sp['pro']+url_sp['allmatch'])
    input_mysql_vh(url_sp['allser']+url_sp['vh']+url_sp['allmatch'])
    # print(type(datetime.datetime.now().strftime('%Y-%m-%d')))
