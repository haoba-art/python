# -*- coding=utf-8 -*-
# @Time: 2023/3/29 16:43
# @AUTHOR: HUI
# @File: re_match2.py
# @software: PyCharm
# 匹配多个字符
import re

# ：匹配出，⼀个字符串第⼀个字⺟为⼤写字符，后⾯都是⼩写字⺟并且这些⼩写字⺟可有可⽆
ret = re.match("[A-Z][a-z]*", "M")
print(ret.group())
ret = re.match("[A-Z][a-z]*", "MnnM")
print(ret.group())
ret = re.match("[A-Z][a-z]*", "Aabcdef")
print(ret.group())
# 匹配出，变量名是否有效
names = ["name1", "_name", "2_name", "__name__"]
for name in names:
    ret = re.match("[a-zA-Z_]+[\w]*", name)
    if ret:
        print("变量名 %s 符合要求" % ret.group())
    else:
        print("变量名 %s ⾮法" % name)
# 匹配出，0到99之间的数字
ret = re.match("[1-9]?[0-9]", "7")
print(ret.group())
ret = re.match("[1-9]?\d", "33")
print(ret.group())
# 这个结果并不是想要的，利⽤$才能解决
ret = re.match("[1-9]?\d", "09")
print(ret.group())
ret = re.match("[a-zA-Z0-9_]{6}", "12a3g45678")
print(ret.group())
# 匹配出，8到20位的密码，可以是⼤⼩写英⽂字⺟、数字、下划线
ret = re.match("[a-zA-Z0-9_]{8,20}", "1ad12f23s34455ff66")
print(ret.group())
