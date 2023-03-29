# -*- coding=utf-8 -*-
# @Time: 2023/3/29 12:14
# @AUTHOR: HUI
# @File: demo1.py
# @software: PyCharm
# ⑤Scale（尺度）用法
import tkinter as tk

root = tk.Tk()
root.title("这是Demo")
root.geometry("300x200")

# root---界面（需要放在那个界面），textvariable----显示文本变量
# bg----背景   font----字体格式，大小    width----宽度   height----高度
l = tk.Label(root, bg='yellow', width=20, text='empty')
l.pack()


def print_selection(v):
    l.config(text='you have selected ' + v)


# Scale----尺度函数
# root---界面（需要放在那个界面），label----标签名字   from_ ----尺度从哪开始    to----尺度到哪结束
# orient----尺度方向（HORIZONTAL水平）   length----显示长度（单位为像素）   tickinterval----每隔多少加个尺度显示
# resolution ----精度（精确到小数点后多少）  command----命令
s = tk.Scale(root, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,
             length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
s.pack()

root.mainloop()
