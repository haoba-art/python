# -*- coding=utf-8 -*-
# @Time: 2023/3/29 16:52
# @AUTHOR: HUI
# @File: re.match4.py.py
# @software: PyCharm
#匹配出0-100之间的数字
import re
ret = re.match("[1-9]?\d$|100","8")
print(ret.group()) # 8
ret = re.match("[1-9]?\d$|100","78")
print(ret.group()) # 78
ret = re.match("[1-9]?\d$|100","08")
# print(ret.group()) # 不是0-100之间
ret = re.match("[1-9]?\d$|100","100")
print(ret.group()) # 100