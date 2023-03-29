# -*- coding=utf-8 -*-
# @Time: 2023/3/29 12:14
# @AUTHOR: HUI
# @File: demo1.py
# @software: PyCharm
# ⑧menubar(菜单栏)
import tkinter as tk

root = tk.Tk()
root.title('my window')
root.geometry('300x300')

# root---界面（需要放在那个界面），textvariable----显示文本变量
# bg----背景   font----字体格式，大小    width----宽度   height----高度
l = tk.Label(root, text='', bg='yellow')
l.pack()
counter = 0


def do_job():
    global counter
    l.config(text='do ' + str(counter))
    counter += 1


# menubar----菜单
menubar = tk.Menu(root)  # 菜单加入root界面
filemenu = tk.Menu(menubar, tearoff=0)  # filemenu加入菜单栏menubar下（tearoff=0 不可分割）
# filemenu菜单加入标签和相应执行命令
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()  # 添加分割线
filemenu.add_command(label='Exit', command=root.quit)

editmenu = tk.Menu(menubar, tearoff=0)  # editmenu加入菜单menubar下（tearoff=0 不可分割）
# editmenu菜单加入标签和相应执行命令
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

# submenu加入菜单filemenu下（tearoff=0 不可分割）
submenu = tk.Menu(filemenu)
# filemenu菜单加入标签和相应执行命令
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
submenu.add_command(label="Submenu1", command=do_job)

# 配置菜单栏
root.config(menu=menubar)

root.mainloop()
