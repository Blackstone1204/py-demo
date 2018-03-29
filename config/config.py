#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-29 11:33:31
# @Author  : blackstone (971406187@qq.com)
# @Do      : 读取配置文件测试


import ConfigParser
#print dir(ConfigParser)


class Configer:
	def __init__(self,path):
		self.cf=ConfigParser.ConfigParser()
		self.cf.read(path)


	def getProp(self,groupName,p):
		return self.cf.get(groupName,p)




if __name__=="__main__":
	cf= Configer("cf.ini")
	print cf.getProp("config","platformName")



