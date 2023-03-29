# -*- coding=utf-8 -*-
# @Time: 2023/3/29 16:46
# @AUTHOR: HUI
# @File: re_match3.py
# @software: PyCharm
# 匹配开头结尾
import re
email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
for email in email_list:
    ret = re.match("[\w]{4,20}@163\.com$", email)
    if ret:
        print("%s 是符合规定的邮件地址,匹配后的结果是:%s" % (email, ret.group()))
    else:
        print("%s 不符合要求" % email)