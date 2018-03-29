#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-27 17:50:08
# @Author  : ${author} (971406187@qq.com)
# @Do      :python 实例方法、静态方法、类方法测试 后两者python2 需标注显示声明 否则调用会报错

class BaseC:
	def im(self):
		print self

	@classmethod
	def cm(cls):
		print cls

class Test(BaseC):

	@staticmethod
	def staticMethod():
		print "call static method"

	@classmethod

	def classMethod(cls ):
		print cls


	def instanceMethod(self):
		print self




if __name__=="__main__":
	print "实例方法测试 "
	t=Test()
	Test.instanceMethod(t)  #实例方法通过类调用时 需显示传入实例
	t.instanceMethod()
	print "静态方法测试 "
	Test.staticMethod()     #同java调用形式
	t.staticMethod()        #  实例方式调用时 @staticmethod 标记的静态方法会自动传入一个self 没标记会报错 
	print "类方法测试 "     #
	Test.classMethod()
	t.classMethod()

	Test.im(t)              #cm im继承自BaseC 打印的selfq却还是Test
	t.im()

	Test.cm()        
	t.cm()


