# -*- coding=utf-8 -*-
# @Time: 2023/3/29 17:12
# @AUTHOR: HUI
# @File: re_compile.py
# @software: PyCharm
import re

pattern = re.compile(r'\d+')
m = pattern.match('one12twothree34four', 3, 10)  # 从'1'的位置开始匹配，正好匹配
print(m)  # 返回一个 Match 对象
res = m.group(0)  # 可省略 0
print(res)
res = m.start(0)  # 可省略 0
print(res)
res = m.end(0)  # 可省略 0
print(res)
res = m.span(0)  # 可省略 0
print(res)
