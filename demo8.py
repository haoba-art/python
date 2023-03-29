# -*- coding=utf-8 -*-
# @Time: 2023/3/29 12:14
# @AUTHOR: HUI
# @File: demo1.py
# @software: PyCharm
# ⑦canvas（画布）用法
import tkinter as tk

root = tk.Tk()
root.title("这是Demo")
root.geometry("300x300")

# Canvas----画布
# root---界面（需要放在那个界面）
# bg----背景     width----宽度，height----高度（单位像素）
canvas = tk.Canvas(root, bg='white', height=200, width=200)

# PhotoImage----加载图片
# 图片路径为file='C:\\Users\\admin\\Desktop\\Demo\\Demo\\1.gif'  注意是使用双斜杆\\
image_file = tk.PhotoImage(file='1.gif')

# create_image----图片位置
# create_image（瞄点横坐标，瞄点纵坐标，瞄点位置，加入图片）
image = canvas.create_image(0, 0, anchor='nw', image=image_file)

# create_line----画线
# create_oval----画圆
# create_arc----画扇形
# create_rectangle----画矩形
# canvas.create_oval
x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)
# create_oval----画扇形
# create_oval（坐标，坐标，坐标，坐标，填充颜色）
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
# create_oval----画圆
# create_oval（坐标，坐标，坐标，坐标，开始角度，结束角度）
arc = canvas.create_arc(x0 + 30, y0 + 30, x1 + 30, y1 + 30, start=90, extent=180)
rect = canvas.create_rectangle(100, 30, 100 + 20, 30 + 20)
canvas.pack()


# move----移动
# canvas.move(对象, 横坐标, 纵坐标)
def moveit():
    canvas.move(rect, 2, 4)


b = tk.Button(root, text='move', command=moveit).pack()

root.mainloop()
