# -*- coding=utf-8 -*-
# @Time: 2023/3/29 16:53
# @AUTHOR: HUI
# @File: re.match7.py.py
# @software: PyCharm
import re
labels = ["<html><h1>www.itcast.cn</h1></html>", "<html><h1>www.itcast.cn</h2></html>"]
for label in labels:
    ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", label)
    if ret:
        print("%s 是符合要求的标签" % ret.group())
    else:
        print("%s 不符合要求" % label)