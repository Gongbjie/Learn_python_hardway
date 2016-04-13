#!/usr/bin/python
# -- coding: utf8 --
print "How old are you?", # 加上逗号,print就不会输出新行符而结束这一行跑到下一行去了
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So you're %r old, %r tall and %r heavy." % (age, height, weight)
