#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-28 17:13:22
# @Author  : blackstone (971406187@qq.com)
# @Do      :


import subprocess

obj=subprocess.Popen("python",stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

obj.stdin.write("print1 'hello' ")
obj.stdin.close()  #没这行 输入没返回

cmdout=obj.stdout.read()
obj.stdout.close()
print "msg ",cmdout

cmderr=obj.stderr.read()
obj.stderr.close()

print "error ",cmderr
