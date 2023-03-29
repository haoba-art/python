# -*- coding=utf-8 -*-
# @Time: 2023/3/29 16:53
# @AUTHOR: HUI
# @File: re.match8.py
# @software: PyCharm
import re
ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>","<html><h1>www.itcast.cn</h1></html>")
ret.group()
print(ret)
ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>","<html><h1>www.itcast.cn</h2></html>")
# ret.group()
print(ret)