# -*- coding=utf-8 -*-
# @Time: 2023/3/29 12:14
# @AUTHOR: HUI
# @File: demo1.py
# @software: PyCharm
# ③var（变量）和list（列表）用法
import tkinter as tk

root = tk.Tk()
root.title("这是Demo")
root.geometry("300x200")

# root---界面（需要放在那个界面），textvariable----显示文本变量
# bg----背景   font----字体格式，大小    width----宽度   height----高度
var1 = tk.StringVar()
l = tk.Label(root, bg='yellow', width=4, textvariable=var1)
l.pack()


def print_selection():
    value = lb.get(lb.curselection())  # 获取列表选项
    var1.set(value)  # 设置textvariable=var1的文本值


# root---界面（需要放在那个界面），text----显示文本
# width----宽度   height----高度  command----命令（执行哪个函数）
b1 = tk.Button(root, text="print selection", width=15, height=2, command=print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))
# root---界面（需要放在那个界面），listvariable----列表变量
lb = tk.Listbox(root, listvariable=var2)  # 列表变量var2
list_items = [1, 2, 3, 4]

for item in list_items:  # 列表遍历
    lb.insert('end', item)
lb.insert(1, 'first')  # 1号位后加入first
lb.insert(2, 'second')  # 2号位后加入second
# lb.delete(2) #删除2后的second
lb.pack()

root.mainloop()
