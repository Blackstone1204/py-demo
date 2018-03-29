#coding=utf-8


string ="test it";
fvalue=1.0
ivalue=2L


print string,fvalue,ivalue

print "********列表操作*******"

alist=['a','b','c']
blist=['d','e']

print alist[1:]
print blist[0:3]
print alist+blist
print alist*2

print "*******元组操作*********"
ctuple=(1,2,3)
dtuple=(4,5)
print ctuple
print ctuple[2:]
print ctuple+dtuple
print dtuple*2

ctuple[2]=99#元组二次赋值非法
