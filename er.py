# -*- coding=utf-8 -*-
# @Time: 2021/11/1 17:41
# @AUTHOR: HUI
# @File: er.py
# @software: PyCharm

from MyQR import myqr
from PIL import Image
import matplotlib.pyplot as plt
import os
dir_path = os.path.dirname(__file__)
myqr.run(
    words='hui',
    # 扫描二维码后，显示的内容，或是跳转的链接
    version=5,  # 设置容错率
    # level='H',  # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
    picture='1.gif',  # 图片所在目录，可以是动图
    colorized=True,  # 黑白(False)还是彩色(True)
    # contrast=1.0,  # 用以调节图片的对比度，1.0 表示原始图片。默认为1.0。
    # brightness=1.0,  # 用来调节图片的亮度，用法同上。
    save_name='4.gif',  # 控制输出文件名，格式可以是 .jpg， .png ，.bmp ，.gif
    save_dir=dir_path,# 图片存储位置
)
img = Image.open('4.gif') # 读取所保存的图片展示二维码
plt.figure("Image") # 图像窗口名称
plt.imshow(img)
plt.axis('off') # 关掉坐标轴为 off
plt.show()