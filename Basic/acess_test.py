#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-27 17:35:20
# @Author  : blackstone (971406187@qq.com)
# @Link    : ${link}
# @Version : _ __ startwith可见性测试

from acess import *

b=base()
#base.__b      #会报错
base._base__b  #私有变量还是可以通过这种方式调用