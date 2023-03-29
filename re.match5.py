# -*- coding=utf-8 -*-
# @Time: 2023/3/29 16:53
# @AUTHOR: HUI
# @File: re.match5.py.py
# @software: PyCharm
import re

# 需求：匹配出163、126、qq邮箱
ret = re.match("\w{4,20}@163\.com", "test@163.com")
print(ret.group())  # test@163.com
ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@126.com")
print(ret.group())  # test@126.com
ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@qq.com")
print(ret.group())  # test@qq.com
ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@gmail.com")
if ret:
    print(ret.group())
else:
    print("不是163、126、qq邮箱")  # 不是163、126、qq邮箱
# 不是以4、7结尾的⼿机号码(11位)
tels = ["13100001234", "18912344321", "10086", "18800007777"]
for tel in tels:
    ret = re.match("1\d{9}[0-35-68-9]", tel)
    if ret:
        print(ret.group())
    else:
        print("%s 不是想要的⼿机号" % tel)
# 提取区号和电话号码
ret = re.match("([^-]*)-(\d+)", "010-12345678")
print(ret.group())
print(ret.group(1))
print(ret.group(2))
