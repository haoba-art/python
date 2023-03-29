# -*- coding=utf-8 -*-
# @Time: 2022/7/20 17:27
# @AUTHOR: HUI
# @File: tttt.py
# @software: PyCharm
# python3 author linzhongyunwu

import time
from PIL import ImageGrab
import os

# 在没有png目录时，创建一个png目录
absPath = os.path.abspath('.')
path = [x for x in os.listdir('.') if os.path.isdir(x)]
# print(path)
if 'png' in path:
    # print('yes')
    pass
else:
    # print('no')
    # 创建目录
    pngPath = os.path.join(absPath, 'png')
    os.mkdir(pngPath)


# 截屏
def Screening():
    nowtime = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    print(nowtime)
    # 截屏
    im = ImageGrab.grab()
    # 保存
    im.save(r'png\%s.png' % (nowtime))


count = 1
while count <= 10:
    print(count)
    Screening()
    count += 1
    time.sleep(5)  # 定时10s看一下
