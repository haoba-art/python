# -*- coding=utf-8 -*-
# @Time: 2023/3/29 17:34
# @AUTHOR: HUI
# @File: re_other.py
# @software: PyCharm
import re

# re.search
ret = re.search(r"\d+", "阅读次数为9999")
print(ret.group())

# re.findall
ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
print(ret)

# re.finditer
it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())

# re.sub
ret = re.sub(r"\d+", '998', "python = 997")
print(ret)


def add(temp):
    # int（）参数必须是字符串，类似字节的对象或数字，而不是“re.Match”
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)


ret = re.sub(r"\d+", add, "python = 997")
print(ret)
ret = re.sub(r"\d+", add, "python = 99")
print(ret)
# re.subn
pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print(re.subn(pattern, r'\2 \1', s))


def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()


print(re.subn(pattern, func, s))

# re.split
ret = re.split(r":| ","info:xiaoZhang 33 shandong")
print(ret)

# 贪婪匹配
s="This is a number 234-235-22-423"
#正则表达式模式中使⽤到通配字，那它在从左到右的顺序求值时，会尽量“抓取”满⾜匹配最⻓字符串，在我们上⾯的例⼦⾥⾯，“.+”会从字符串的启始处抓取满⾜模式的最⻓字符，其中包括我们想得到的第⼀个整型字段的中的⼤部分，“\d+”只需⼀位字符就可以匹配，所以它匹配了数字“4”，⽽“.+”则匹配了从字符串起始到这个第⼀位数字4之前的所有字符
r=re.match(".+(\d+-\d+-\d+-\d+)",s)
print(r.group(1))
#⾮贪婪操作符“？”，这个操作符可以⽤在"*","+","?"的后⾯，要求正则匹配的越少越好
r=re.match(".+?(\d+-\d+-\d+-\d+)",s)
print(r.group(1))

res = re.match(r"aa(\d+)","aa2343ddd").group(1)
print(res)
res = re.match(r"aa(\d+?)","aa2343ddd").group(1)
print(res)
res = re.match(r"aa(\d+)ddd","aa2343ddd").group(1)
print(res)
res = re.match(r"aa(\d+?)ddd","aa2343ddd").group(1)
print(res)

test_str="<img data-original=https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973.jpg>"
ret = re.search(r"https://.*?.jpg", test_str)
print(ret.group())