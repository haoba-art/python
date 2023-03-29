# -*- coding=utf-8 -*-
# @Time: 2023/3/29 12:14
# @AUTHOR: HUI
# @File: demo1.py
# @software: PyCharm
# 窗口内的组件布局
import tkinter as tk  # tk代替tkinter
from tkinter import messagebox

root = tk.Tk()  # 创建窗口
root.title('演示窗口')
root.geometry("300x100+630+80")  # 长x宽+x*y
btn1 = tk.Button(root)  # 创建按钮，并且将按钮放到窗口里面
btn1["text"] = "点击"  # 给按钮一个名称
btn1.pack()  # 按钮布局


def test(e):
    # 创建弹窗
    messagebox.showinfo("窗口名称", "点击成功")


btn1.bind("<Button-1>", test)  # 将按钮和方法进行绑定，也就是创建了一个事件
root.mainloop()  # 让窗口一直显示，循环