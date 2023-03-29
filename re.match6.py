# -*- coding=utf-8 -*-
# @Time: 2023/3/29 16:53
# @AUTHOR: HUI
# @File: re.match6.py.py
# @software: PyCharm
import re
# 正确的理解思路：如果在第⼀对<>中是什么，按理说在后⾯的那对<>中就应该是什么。通过引⽤分组中匹配到的数据即可，但是要注意是元字符串，即类似 r""这种格式。
ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
# 因为2对<>中的数据不⼀致，所以没有匹配出来
test_label = ["<html>hh</html>","<html>hh</htmlbalabala>"]
for label in test_label:
    ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", label)
    if ret:
        print("%s 这是一对正确的标签" % ret.group())
    else:
        print("%s 这是⼀对不正确的标签" % label)