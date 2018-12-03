import pymysql

db = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='jhczxcvbnm',
    db='test',
    charset='utf8'
)


# 获取游标
cursor = db.cursor()

sql='select * from table1'
try:
    cursor.execute(sql)
    results=cursor.fetchall()
    print('1','2','3','4')
    for row in results:
        one=row[0]
        two=row[1]
        three=row[2]
        four=row[3]
        print(one,two,three,four)
except Exception as e:
    raise e
db.close()