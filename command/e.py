#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-28 18:29:12
# @Author  : blackstone (971406187@qq.com)
# @Do      :命令行测试 cwd参数


#报错

import subprocess
obj=subprocess.Popen("mkdir test",cwd="./root",stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
print obj.communicate()
