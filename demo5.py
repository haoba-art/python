# -*- coding=utf-8 -*-
# @Time: 2023/3/29 12:14
# @AUTHOR: HUI
# @File: demo1.py
# @software: PyCharm
# ④Radiobutton(选择按钮)用法
import tkinter as tk

root = tk.Tk()
root.title("这是Demo")
root.geometry("300x200")

# root---界面（需要放在那个界面），textvariable----显示文本变量
# bg----背景   font----字体格式，大小    width----宽度   height----高度
var = tk.StringVar()
l = tk.Label(root, bg='yellow', width=20, text='empty')
l.pack()


def print_selection():
    l.config(text='you have selected ' + var.get())


# Radiobutton-----选择按钮
# root---界面（需要放在那个界面），variable----变量
# value----值   command----命令
r1 = tk.Radiobutton(root, text='Option A',
                    variable=var, value='A',
                    command=print_selection)
r1.pack()
r2 = tk.Radiobutton(root, text='Option B',
                    variable=var, value='B',
                    command=print_selection)
r2.pack()
r3 = tk.Radiobutton(root, text='Option C',
                    variable=var, value='C',
                    command=print_selection)
r3.pack()

root.mainloop()
