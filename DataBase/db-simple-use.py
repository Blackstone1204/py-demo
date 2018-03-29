#coding=utf-8
import time
import pymysql


# 连接MySQL数据库
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='tryme', db='auto', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)


# 通过cursor创建游标
cursor = connection.cursor()

# 执行数据查询
sql = "select * from user"
cursor.execute(sql)

#查询数据库单条数据
result = cursor.fetchone()
print("-----------单条数据查询------------")
print(result)



# 执行数据查询
sql = "select * from user"
cursor.execute(sql)

#查询数据库多条数据
print("-----------多条数据查询------------")
result = cursor.fetchall()
for data in result:
    print(data)



#插入操作
print("-----------插入操作------------")
sql="insert into user(user_name,password,role_id) values('guest','123456','')"

cursor.execute(sql);
connection.commit();

#更新操作
print("-----------更新操作------------")
sql="update user set role_id=7 where user_name ='guest'"
cursor.execute(sql)
connection.commit()

#删除操作
print("-----------删除操作------------")
sql="delete from user where user_name ='guest'"
cursor.execute(sql)
connection.commit()

# 关闭数据连接
connection.close()