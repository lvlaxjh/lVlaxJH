import pymysql

db = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='jhczxcvbnm',
    db='dota2data',
    charset='utf8'
)


cursor=db.cursor()

# SQL 插入语句
sql ='''insert into dota2data(heroname,alluse,allwin,state,times) values ("%s","%s","%s","%s","%s")'''% \
     ('1','2','3','4','6')

try:
# 执行sql语句
    cursor.execute(sql)
    # 执行sql语句
    db.commit()
except:
   # 发生错误时回滚
   print('error')
   db.rollback()

sql = "DELETE FROM `dota2data` WHERE (`heroname`='1') AND (`alluse`='2') AND (`allwin`='3') AND (`state`='4') AND (`times`='5') LIMIT 1"
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()


sql = "SELECT * FROM dota2data"

try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()

   print(results)
except:
   print ("Error: unable to fecth data")

db.close()