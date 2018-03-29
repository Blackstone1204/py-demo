#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-28 18:01:55
# @Author  : blackstone (971406187@qq.com)
# @Do      :命令行测试


import subprocess
#
obj1=subprocess.Popen(["netstat","-ano"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
obj2=subprocess.Popen("findstr 127",stdin=obj1.stdout,stdout=subprocess.PIPE)
print obj2.communicate()







