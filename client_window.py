# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

from tkinter import *
import tkinter.messagebox
import arrow
import tkinter.filedialog
import git_base
import log_utils
import version_tools_cmft as cmft_tools

logger = log_utils.get_logger()


# 一键创建下周分支
def auto_create_branch(event):
    log_utils.clear_log_content()
    # 创建下周分支
    cmft_tools.create_next_week_branch(1174)

    logs_content = log_utils.read_logs()

    clear_text_area()

    append_text_to_text_area(logs_content)
    # 清空日志信息
    log_utils.clear_log_content()


# 清空text_area信息
def clear_text_area():
    text_area.delete(0.0, END)


# 向text_area追加内容
def append_text_to_text_area(text_content):
    text_area.insert('end', text_content)
    text_area.mark_set('insert', 'end')


# 冻结版本
def freeze_version(event):
    append_text_to_text_area('hello\n')


# 选择项目文件目录
def choose_project_path(event):
    log_utils.clear_log_content()
    text_area.delete(0.0, END)
    path = tkinter.filedialog.askdirectory()
    if path != '':
        logger.info('工作目录为:' + path)
        work_path_label.config(text=path)
        result, stdout, stderr = git_base.check_local_branch(path)
        logs_content = log_utils.read_logs()
        text_area.insert(1.0, logs_content)
    else:
        work_path_label.config(text="您没有选择任何目录")


# 创建窗口程序
root = Tk()
root.title('CMFT Git Tools')
root.resizable(False, False)

# head icon
icon = PhotoImage(file='resource/cmft_logo.gif')
label = Label(image=icon)
label.image = icon
label.grid(row=0, column=0, columnspan=3, sticky=W + E + N + S, padx=5, pady=5)

Label(root, text='当前时间:').grid(row=1, column=0, padx=5, pady=5, sticky=W)
Label(
    root, text=arrow.now().format('YYYY-MM-DD(ddd) HH:MM')).grid(
        row=1, column=1, padx=5, pady=5, sticky=W)

Label(
    root, text='Access Token:').grid(
        row=2, column=0, padx=5, pady=5, sticky=W)

work_path_label = Label(root, text='请设置access token', relief=GROOVE, width=30)
work_path_label.grid(row=2, column=1, padx=5, pady=5, sticky=W)

create_next_branch_button = Button(root, text="一键创建下周版本", width=15)
create_next_branch_button.bind('<Button-1>', auto_create_branch)
create_next_branch_button.grid(row=3, column=1, pady=5, sticky=W)

Label(root, text='版本冻结:').grid(row=4, column=0, padx=5, pady=5, sticky=W)

work_path_label = Label(root, text='请选择需要冻结的版本', relief=GROOVE, width=30)
work_path_label.grid(row=4, column=1, padx=5, pady=5, sticky=W)

freeze_version_button = Button(root, text="冻结所选版本", width=15)
freeze_version_button.bind('<Button-1>', freeze_version)
freeze_version_button.grid(row=5, column=1, pady=5, sticky=W)

Label(root, text='结果:').grid(row=6, column=0, columnspan=2, sticky=W)

text_area = Text(root, background='grey')
text_area.grid(row=7, column=0, columnspan=3)
root.mainloop()