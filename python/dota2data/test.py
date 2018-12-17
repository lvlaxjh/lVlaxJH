import pymysql

from sshtunnel import SSHTunnelForwarder

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
cursor=db.cursor()

dota2_data={'all':'dota2dataall',
            'vh':'dota2datavh',
            'pro':'dota2datapro'}
sql = "SELECT * FROM %s" % dota2_data['pro']

# 执行SQL语句
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()
all_data_tub=results
for i in all_data_tub:
    for n in i:
        print(n)

db.close()