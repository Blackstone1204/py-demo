#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-28 17:15:11
# @Author  : blackstone (971406187@qq.com)
# @Do      :命令行交互测试


import subprocess

try:
	obj=subprocess.Popen("java1 -version",stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	back=obj.communicate()
	print back,len(back)

except:
	pass












  #返回长度=2 元组

