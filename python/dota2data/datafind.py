import pymysql

from sshtunnel import SSHTunnelForwarder

###############################
now_day = '2018-12-14'
###############################
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

dota2_data = {'all': 'dota2dataall',
              'vh': 'dota2datavh',
              'pro': 'dota2datapro'}
sql = "SELECT * FROM %s" % dota2_data['vh']

# 执行SQL语句
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()
all_data_tub = results
all_hero_datas = {}
for i in all_data_tub:
    if i[13] == now_day:
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
name_list=['win','use','gpm','epm','kda','k','d','a','dmg','treat','arc']
flag=0
flag2=1
all_data_float=0.0
for i in all_sort_list:
    print(name_list[flag])
    for n in i:
        # print(n[1][flag])
        all_data_float=all_data_float+n[1][flag]
    # print(all_data_float)
    print(all_data_float//len(i))
    all_data_float=0.0
    for a in range(10):
        print(i[a][0],i[a][1][flag])
    print('----------------')
    for a in range(len(i)-1,-1,-1):
        flag2+=1
        print(i[a][0],i[a][1][flag])
        if flag2==6:
            flag2=1
            break;
    flag+=1

