import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root',
                       password='Wjl62300313.', db='sqltest')
# cur = conn.cursor()
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 指定返回为dict
# 插入
# sql_1 = "insert into child values(%s, %s, %s)"
# param = (40, 2, 3)
# recount = cur.execute(sql_1, param)

# sql_2 = 'insert into child values(%s, %s, %s)'
# params = [(15, 234, 2), (90, 222, 1)]
# recount = cur.executemany(sql_2, params)
sql_1 = "insert into child values(%(id)s, %(age)s, %(pid)s)"
values = {
    'id': 13,
    'age': 22,
    'pid': 2
}
cur.execute(sql_1, values)
conn.commit()  # 提交，执行多条命令只需要commit一次就行了
# 查询
id = (13,)
# 参数化查询
sql = 'select * from child where id = %s'
# 执行sql语句
recount = cur.execute(sql, id)  # 返回受影响行数
print(recount)
# 查询多条数据 fetone 1条数据
#data = cur.fetchall()
data = cur.fetchmany(2)
for dat in data:
    print(dat)

cur.close()
conn.close()


