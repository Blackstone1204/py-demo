#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-28 15:38:11
# @Author  : blackstone (971406187@qq.com)
# @Do      :


import logging



LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

#logging.basicConfig(filename='my.log',level=logging.DEBUG,format=LOG_FORMAT)
logging.basicConfig(level=logging.DEBUG,format=LOG_FORMAT)
logging.debug("debug")
logging.error("fjdlafdjlfd")

