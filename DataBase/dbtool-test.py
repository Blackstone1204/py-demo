#coding=utf-8
import dbtool


dt=dbtool.dbtool()
dt.connect('localhost',3306,'root','tryme','auto')

objs=dt.queryObjs("select * from user")
for obj in objs:
	print obj,obj["user_name"]