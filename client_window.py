# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

from tkinter import *
import tkinter.messagebox
import arrow
import tkinter.filedialog
import git_base


# 一键创建下周分支
def auto_create_branch(event):
    print('hello')


# 选择项目文件目录
def choose_project_path(event):
    path = tkinter.filedialog.askdirectory()
    if path != '':
        print('工作目录为:', path)
        work_path_label.config(text=path)
        result, stdout, stderr = git_base.check_local_branch(path)
        text_area.insert(1.0,stdout)
        current_branch_label.config(text=get_current_branch(stdout))
    else:
        work_path_label.config(text="您没有选择任何目录")


# 根据stdout获取当前分支
def get_current_branch(stdout):
    if (stdout != ''):
        start_index = stdout.find('*')
        end_index = stdout.find('\n')
        print('当前分支：', stdout[start_index + 2:end_index])
    else:
        print('stdout为空！')
    return stdout[start_index + 2:end_index]


# 创建窗口程序
root = Tk()
root.title('CMFT Git Tools')
root.resizable(False, False)

Label(root, text='当前时间:').grid(row=0, column=0, padx=5, pady=5)
Label(
    root, text=arrow.now().format('YYYY-MM-DD/HH:MM:SS')).grid(
        row=0, column=1, padx=5, pady=5, sticky=W)

Label(root, text='工程目录:').grid(row=1, column=0, padx=5, pady=5)
work_path_label = Label(root, text='请选择项目工程目录', relief=GROOVE, width=40)
work_path_label.grid(row=1, column=1, padx=5, pady=5, sticky=W)

choose_project_btn = Button(root, text='选择工程目录', width=20)
choose_project_btn.bind('<Button-1>', choose_project_path)
choose_project_btn.grid(row=2, column=1, padx=5, pady=5, sticky=W)

Label(root, text='当前分支:').grid(row=3, column=0, padx=5, pady=5)
current_branch_label = Label(root, text='暂未读取到分支信息', relief=GROOVE, width=40)
current_branch_label.grid(row=3, column=1, padx=5, pady=5, sticky=W)

icon = PhotoImage(file='resource/cmft_logo.gif')
label = Label(image=icon)
label.image = icon
label.grid(
    row=0,
    column=2,
    columnspan=2,
    rowspan=4,
    sticky=W + E + N + S,
    padx=5,
    pady=5)

b1 = Button(root, text="一键创建下周分支", width=20)
b1.bind('<Button-1>', auto_create_branch)
b1.grid(row=4, column=1, padx=5, pady=5, columnspan=2, sticky=W)

Label(root, text='结果:').grid(row=5, column=0, columnspan=3,sticky=W)
work_path_label.grid(row=1, column=1, padx=5, pady=5, sticky=W)

text_area = Text(root,background='grey')
text_area.grid(row=6, column=0, columnspan=3)
root.mainloop()