# -*- coding=utf-8 -*-
# @Time: 2023/3/29 12:14
# @AUTHOR: HUI
# @File: demo1.py
# @software: PyCharm
# ⑥ Checkbutton（勾选项）用法
import tkinter as tk

root = tk.Tk()
root.title("这是Demo")
root.geometry("300x200")

# root---界面（需要放在那个界面），textvariable----显示文本变量
# bg----背景   font----字体格式，大小    width----宽度   height----高度
l = tk.Label(root, bg='yellow', width=20, text='empty')
l.pack()


def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love only Python ')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')


var1 = tk.IntVar()
var2 = tk.IntVar()

# Checkbutton----勾选函数
# root---界面（需要放在那个界面），text----文本   variable ----变量
# onvalue----勾选标志值   offvalue----无勾选标志值   command----命令
c1 = tk.Checkbutton(root, text='Python', variable=var1, onvalue=1, offvalue=0,
                    command=print_selection)
c2 = tk.Checkbutton(root, text='C++', variable=var2, onvalue=1, offvalue=0,
                    command=print_selection)
c1.pack()
c2.pack()

root.mainloop()
