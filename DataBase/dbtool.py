# coding=utf-8
import pymysql


class dbtool:

# 连接操作
	def connect(self, host, port, user, password, db):
		self.connection = pymysql.connect(host=host, port=port, user=user, password=password,
		                                  db=db, charset='utf8', cursorclass=pymysql.cursors.DictCursor)
		self.cursor = self.connection.cursor()

		return self.cursor


# 查询操作
	def queryObjs(self,sql):
		try:
			self.cursor.execute(sql)
			return self.cursor.fetchall();

		except e:
			print e

#增删改操作
	def adu(self,sql):
		try:
			self.cursor.execute(sql)
			self.connection.commit()

		except e:
			print e




### My  Test ####################
"""
dt=dbtool()
dt.connect('localhost',3306,'root','tryme','auto')
users=dt.queryAll("select * from user");
for user in users:
	print user["user_name"]


dt.adu("update user set password='1223' where user_name like 'root'")
#dt.adu("update user set password='3444' where user_name='admin'")

"""












