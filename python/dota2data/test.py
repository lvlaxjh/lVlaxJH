import pymysql

db = pymysql.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='jhczxcvbnm',
    db='dota2data',
    charset='utf8'
)
cursor = db.cursor()

sql = "SELECT * FROM %s" % 'dota2dataall'

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
while(True):
    results = cursor.fetchone()
    if results!=None:
        all_data_tub = results
        if all_data_tub[13] == '2018-12-14':
            all_hero_datas[all_data_tub[0]] = [all_data_tub[1], all_data_tub[2], all_data_tub[3], all_data_tub[4],
                                               all_data_tub[5], all_data_tub[6], all_data_tub[7], all_data_tub[8],
                                               all_data_tub[9], all_data_tub[10], all_data_tub[11], all_data_tub[12],
                                               all_data_tub[13]]
    else:
        break
db.close()