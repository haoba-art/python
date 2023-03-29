# -*- coding=utf-8 -*-
# @Time: 2023/3/29 16:39
# @AUTHOR: HUI
# @File: re_match1.py
# @software: PyCharm
# 匹配单个字符
import re
ret = re.match(".","M")
print(ret.group())
ret = re.match("t.o","too")
print(ret.group())
ret = re.match("t.o","two")
print(ret.group())
# 如果hello的⾸字符⼩写，那么正则表达式需要⼩写的h
ret = re.match("h","hello Python")
print(ret.group())
# 如果hello的⾸字符⼤写，那么正则表达式需要⼤写的H
ret = re.match("H","Hello Python")
print(ret.group())
# ⼤⼩写h都可以的情况
ret = re.match("[hH]","hello Python")
print(ret.group())
ret = re.match("[hH]","Hello Python")
print(ret.group())
ret = re.match("[hH]ello Python","Hello Python")
print(ret.group())
# 匹配0到9的多种写法
ret = re.match("[0123456789]Hello Python","7Hello Python")
print(ret.group())
ret = re.match("[0-9]Hello Python","7Hello Python")
print(ret.group())
# 匹配0到3和5-9
ret = re.match("[0-35-9]Hello Python","7Hello Python")
print(ret.group())
ret = re.match("[0-35-9]Hello Python","4Hello Python")
#print(ret.group())
ret = re.match("嫦娥\d号","嫦娥1号发射成功")
print(ret.group())
ret = re.match("嫦娥\d号","嫦娥2号发射成功")
print(ret.group())