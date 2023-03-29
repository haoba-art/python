# -*- coding=utf-8 -*-
# @Time: 2023/3/29 14:53
# @AUTHOR: HUI
# @File: demo11.py
# @software: PyCharm
# ⑩messagebox(弹窗)
import tkinter as tk
import tkinter.messagebox
root = tk.Tk()
root.title('my window')
root.geometry('200x200')


def hit_me():
    #tk.messagebox.showinfo(title='Hi', message='hahahaha')   # return 'ok'
    #tk.messagebox.showwarning(title='Hi', message='nononono')   #警告 return 'ok'
    # tk.messagebox.showerror(title='Hi', message='No!! never')   #错误 return 'ok'
    #print(tk.messagebox.askquestion(title='Hi', message='hahahaha'))   #询问 return 'yes' , 'no'
    #print(tk.messagebox.askyesno(title='Hi', message='hahahaha'))   #是否 return True, False
    #print(tk.messagebox.askretrycancel(title='Hi', message='hahahaha'))   # 重试  return True, False
    #print(tk.messagebox.askokcancel(title='Hi', message='hahahaha'))   # return True, False
    print(tk.messagebox.askyesnocancel(title="Hi", message="haha"))     # return, True, False, None

tk.Button(root,text = 'hit_me',command=hit_me).pack()

root.mainloop()