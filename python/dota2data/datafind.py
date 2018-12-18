import pymysql
import datetime
from sshtunnel import SSHTunnelForwarder


# data_list数据结构:all_sort_list = [sort_win, sort_use, sort_gpm, sort_epm, sort_kda, sort_k, sort_d, sort_a, sort_dmg, sort_treat,sort_arc]


def get_data(what_data, nowday):
    # 远程连接数据库获取数据
    with SSHTunnelForwarder(
            ('47.93.36.54', 22),  # B机器的配置
            ssh_password="jhczxcvbnm0325!!!",
            ssh_username="root",
            remote_bind_address=('127.0.0.1', 3306)) as server:  # A机器的配置
        db = pymysql.Connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='jhczxcvbnm',
            db='dota2data',
            charset='utf8'
        )
    cursor = db.cursor()

    sql = "SELECT * FROM %s" % what_data

    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    all_data_tub = results
    all_hero_datas = {}
    for i in all_data_tub:
        if i[13] == nowday:
            all_hero_datas[i[0]] = [i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13]]
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
    # {'****':[win,use,gpm,epm,kda,k,d,a,dmg,treat,arc]}
    return all_sort_list


def data_cleaning(sort_list, _file):
    name_list = ['win', 'use', 'gpm', 'epm', 'kda', 'k', 'd', 'a', 'dmg', 'treat', 'arc']
    flag = 0
    flag2 = 1
    all_data_float = 0.0
    positive_ranking = 10
    negative_ranking = 5
    for i in sort_list:
        print(name_list[flag])
        _file.write(name_list[flag])
        _file.write('\n')
        for n in i:
            # print(n[1][flag])
            all_data_float = all_data_float + n[1][flag]
        # print(all_data_float)
        print(all_data_float // len(i))
        _file.write((str)(all_data_float // len(i)))
        _file.write('\n')
        all_data_float = 0.0
        for a in range(positive_ranking):
            print(i[a][0], i[a][1])
            _file.write((str)(i[a][0]))
            _file.write((str)(i[a][1]))
            _file.write('\n')
        print('----------------')
        _file.write('----------------' + '\n')
        for a in range(len(i) - 1, -1, -1):
            flag2 += 1
            print(i[a][0], i[a][1])
            _file.write((str)(i[a][0]))
            _file.write((str)(i[a][1]))
            _file.write('\n')
            if flag2 == negative_ranking + 1:
                flag2 = 1
                break;
        flag += 1


def recommend_hero_in_TT(_data_list):
    according_to_use_list = _data_list[1]
    use_20_list = []
    for i in range(20):
        use_20_list.append(according_to_use_list[i])
    get_win_average = 0.0
    for i in use_20_list:
        get_win_average = get_win_average + i[1][0]
    get_win_average = get_win_average / 20
    maybe_recommend_list = []
    for i in use_20_list:
        if i[1][0] > get_win_average:
            maybe_recommend_list.append(i)
    get_use_average = 0.0
    for i in maybe_recommend_list:
        get_use_average = get_use_average + i[1][1]
    get_use_average = get_use_average / len(maybe_recommend_list)
    high_probability_recommend = []
    for i in maybe_recommend_list:
        if i[1][1] > get_use_average:
            high_probability_recommend.append(i)
    true_recommend = []
    true_recommend = sorted(high_probability_recommend, key=lambda x: x[1][0])
    true_recommend.reverse()
    most_true_recommend = true_recommend
    # print(most_true_recommend)
    return most_true_recommend


def data_calculation(_data, _file):
    times = datetime.datetime.now().strftime('%Y-%m-%d')
    _file.write('更新时间---' + times + '\n')
    dota2_data = {'all': 'dota2dataall',
                  'vh': 'dota2datavh',
                  'pro': 'dota2datapro'}

    data_all_sort_list = get_data(dota2_data['all'], now_day)
    data_vh_sort_list = get_data(dota2_data['vh'], now_day)
    data_pro_sort_list = get_data(dota2_data['pro'], now_day)
    print('---全部比赛---')
    _file.write('---全部比赛------------------------------' + '\n')
    data_cleaning(data_all_sort_list, _file)
    print('---天梯高分局---')
    _file.write('---天梯高分局------------------------------' + '\n')
    data_cleaning(data_vh_sort_list, _file)
    print('---职业比赛---')
    _file.write('---职业比赛------------------------------' + '\n')
    data_cleaning(data_pro_sort_list, _file)
    _file.write(
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@' + '\n')
    _file.write(
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@' + '\n')
    _file.write(
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@' + '\n')
    print('天梯上分推荐:')
    _file.write('天梯上分推荐------------------------------' + '\n')
    all_TT = recommend_hero_in_TT(data_all_sort_list)
    for i in all_TT:
        print(i)
        _file.write((str)(i) + '\n')
    print('天梯高分局上分推荐:')
    _file.write('天梯高分局上分推荐------------------------------' + '\n')
    vh_TT = recommend_hero_in_TT(data_vh_sort_list)
    for i in vh_TT:
        print(i)
        _file.write((str)(i) + '\n')


file_new = open('new.txt', 'w+', encoding='UTF-8')
file_old = open('old.txt', 'w+', encoding='UTF-8')

now_day = '2018-12-14'  # !#
day_ago = '2018-12-14'
data_calculation(now_day, file_new)
data_calculation(day_ago, file_old)
file_new.close()
file_old.close()
