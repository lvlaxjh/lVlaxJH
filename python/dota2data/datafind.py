import pymysql
import datetime


# data_list数据结构:all_sort_list = [sort_win, sort_use, sort_gpm, sort_epm, sort_kda, sort_k, sort_d, sort_a, sort_dmg, sort_treat,sort_arc]


def get_data(_what_data, _what_day):
    db = pymysql.Connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='jhczxcvbnm',
        db='dota2data',
        charset='utf8'
    )
    cursor = db.cursor()

    sql = "SELECT * FROM %s" % _what_data

    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchone()
    all_data_tub = results
    all_hero_datas = {}
    if all_data_tub[13] == '2018-12-14':
        all_hero_datas[all_data_tub[0]] = [all_data_tub[1], all_data_tub[2], all_data_tub[3], all_data_tub[4],
                                           all_data_tub[5], all_data_tub[6], all_data_tub[7], all_data_tub[8],
                                           all_data_tub[9], all_data_tub[10], all_data_tub[11], all_data_tub[12],
                                           all_data_tub[13]]
    while (True):
        results = cursor.fetchone()
        if results != None:
            all_data_tub = results
            if all_data_tub[13] == '2018-12-14':
                all_hero_datas[all_data_tub[0]] = [all_data_tub[1], all_data_tub[2], all_data_tub[3], all_data_tub[4],
                                                   all_data_tub[5], all_data_tub[6], all_data_tub[7], all_data_tub[8],
                                                   all_data_tub[9], all_data_tub[10], all_data_tub[11],
                                                   all_data_tub[12],
                                                   all_data_tub[13]]
        else:
            break
    db.close()
    all_sort_list = []
    sort_win = []
    sort_use = []
    sort_gpm = []
    sort_epm = []
    sort_kda = []
    sort_k = []
    sort_d = []
    sort_a = []
    sort_dmg = []
    sort_treat = []
    sort_arc = []
    sort_win = sorted(all_hero_datas.items(), key=lambda x: x[1][0])
    sort_use = sorted(all_hero_datas.items(), key=lambda x: x[1][1])
    sort_gpm = sorted(all_hero_datas.items(), key=lambda x: x[1][2])
    sort_epm = sorted(all_hero_datas.items(), key=lambda x: x[1][3])
    sort_kda = sorted(all_hero_datas.items(), key=lambda x: x[1][4])
    sort_k = sorted(all_hero_datas.items(), key=lambda x: x[1][5])
    sort_d = sorted(all_hero_datas.items(), key=lambda x: x[1][6])
    sort_a = sorted(all_hero_datas.items(), key=lambda x: x[1][7])
    sort_dmg = sorted(all_hero_datas.items(), key=lambda x: x[1][8])
    sort_treat = sorted(all_hero_datas.items(), key=lambda x: x[1][9])
    sort_arc = sorted(all_hero_datas.items(), key=lambda x: x[1][10])
    sort_win.reverse()
    sort_use.reverse()
    sort_gpm.reverse()
    sort_epm.reverse()
    sort_kda.reverse()
    sort_k.reverse()
    sort_d.reverse()
    sort_a.reverse()
    sort_dmg.reverse()
    sort_treat.reverse()
    sort_arc.reverse()
    all_sort_list = [sort_win, sort_use, sort_gpm, sort_epm, sort_kda, sort_k, sort_d, sort_a, sort_dmg, sort_treat,
                     sort_arc]
    return all_sort_list

def recommend_hero_in_TT(_data_list):
    pass

def recommend_hero_carry(_data_list):
    pass

what_data={'all':'dota2dataall',
           'pro':'dota2datapro',
           'vh':'dota2datavh'}

