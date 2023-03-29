# -*- coding=utf-8 -*-
# @Time: 2023/3/29 14:52
# @AUTHOR: HUI
# @File: demo10.py
# @software: PyCharm
# ⑨Frame(架构)
import tkinter as tk

root = tk.Tk()
root.title('my window')
root.geometry('200x200')

# root---界面（需要放在那个界面），textvariable----显示文本变量
# bg----背景   font----字体格式，大小    width----宽度   height----高度
tk.Label(root, text='on the window').pack()

# Frame----框架
# Frame的作用可以合理分布控件位置
# 框架设置在root界面上
frm = tk.Frame(root)
frm.pack()

# 框架设置在Frame框架上（分别在左右）
frm_l = tk.Frame(frm)
frm_r = tk.Frame(frm)
frm_l.pack(side='left')
frm_r.pack(side='right')

tk.Label(frm_l, text='on the frm_l1').pack()
tk.Label(frm_l, text='on the frm_l2').pack()
tk.Label(frm_r, text='on the frm_r1').pack()
root.mainloop()
