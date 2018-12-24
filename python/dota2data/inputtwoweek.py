import pymysql
import datetime

db = pymysql.Connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='jhczxcvbnm',
        db='dota2data',
        charset='utf8'
    )


# times = datetime.datetime.now().strftime('%Y-%m-%d')
cursor = db.cursor()

sql = "delete from dota2dataall where times like '2018-12-14'"

# 执行SQL语句
cursor.execute(sql)

db.close()

file=open('dota2data.html','w+')
inputs=('<p>%s</p>')% '123'
file.writelines(inputs)