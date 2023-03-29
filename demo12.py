# -*- coding=utf-8 -*-
# @Time: 2023/3/29 14:53
# @AUTHOR: HUI
# @File: demo12.py
# @software: PyCharm
# ⑪pack、grid以及place布局用法
import tkinter as tk

root = tk.Tk()
root.title('my window')
root.geometry('200x200')

# canvas = tk.Canvas(window, height=150, width=500)
# canvas.grid(row=1, column=1)
# image_file = tk.PhotoImage(file='welcome.gif')
# image = canvas.create_image(0, 0, anchor='nw', image=image_file)

# pack布局----可以通过side控制放在上下左右
# tk.Label(window, text='1').pack(side='top')
# tk.Label(window, text='1').pack(side='bottom')
# tk.Label(window, text='1').pack(side='left')
# tk.Label(window, text='1').pack(side='right')

# grid布局----通过方格的格式，将控件分布于其中
##for i in range(4):
# for j in range(3):
# tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)

# place布局----通过设置坐标方式，可以精确分布控件
tk.Label(root, text=1).place(x=20, y=10, anchor='nw')

root.mainloop()
