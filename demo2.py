# -*- coding=utf-8 -*-
# @Time: 2023/3/29 12:14
# @AUTHOR: HUI
# @File: demo1.py
# @software: PyCharm
# ①基本界面、label(标签)和button(按钮)用法
import tkinter as tk

root = tk.Tk()
root.title("这是Demo")
root.geometry("300x200")
var = tk.StringVar()  # tk专有字符串
# root---界面（需要放在那个界面），textvariable----显示文本
# bg----背景   font----字体格式，大小    width----宽度   height----高度
lab = tk.Label(root, textvariable=var, bg='green', font=('Arial', 12), width=15, height=2)
lab.pack()  # 把标签置入root界面布局
on_hit = True  # 点击标志位


def hit_me():
    global on_hit
    if on_hit == True:
        on_hit = False  # 点击交替
        var.set("you hit me")
    else:
        on_hit = True
        var.set("")


# root---界面（需要放在那个界面），text----显示文本
# width----宽度   height----高度  command----命令（执行哪个函数）
but = tk.Button(root, text="hitme", width=15, height=2, command=hit_me)
but.pack()

root.mainloop()
