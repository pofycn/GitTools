# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

import tkinter as tk
import arrow
import git_base
import log_utils
import version_tools_cmft as cmft_tools

logger = log_utils.get_logger()


# main window
class RootWindow(tk.Tk):
    def __init__(self):
        # 创建窗口程序
        super().__init__()
        self.title('CMFT Git Tools')
        self.resizable(False, False)
        # 程序界面
        self.setup_ui()

    def setup_ui(self):
        # head icon
        icon = tk.PhotoImage(file='resource/cmft_logo.gif')
        label = tk.Label(image=icon)
        label.image = icon
        label.grid(
            row=0,
            column=0,
            columnspan=3,
            sticky=tk.W + tk.E + tk.N + tk.S,
            padx=5,
            pady=5)

        tk.Label(
            self, text='当前时间:').grid(
                row=1, column=0, padx=5, pady=5, sticky=tk.W)
        tk.Label(
            self, text=arrow.now().format('YYYY-MM-DD(ddd) HH:MM')).grid(
                row=1, column=1, padx=5, pady=5, sticky=tk.W)

        tk.Label(
            self, text='Access Token:').grid(
                row=2, column=0, padx=5, pady=5, sticky=tk.W)

        work_path_label = tk.Label(
            self, text='请点击设置access token', relief=tk.GROOVE, width=30)
        work_path_label.bind('<Button-1>', self.set_access_token)
        work_path_label.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        tk.Label(
            self, text='项目名：').grid(
                row=3, column=0, padx=5, pady=5, sticky=tk.W)
        choose_project_label = tk.Label(
            self, text='请点击选择项目进行管理', relief=tk.GROOVE, width=30)
        choose_project_label.bind('<Button-1>', self.set_projects)
        choose_project_label.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        create_next_branch_button = tk.Button(self, text="一键创建下周版本", width=15)
        create_next_branch_button.bind('<Button-1>', self.auto_create_branch)
        create_next_branch_button.grid(row=4, column=1, pady=5, sticky=tk.W)

        tk.Label(
            self, text='版本冻结:').grid(
                row=5, column=0, padx=5, pady=5, sticky=tk.W)

        work_path_label = tk.Label(
            self, text='请点击选择需要冻结的版本', relief=tk.GROOVE, width=30)
        work_path_label.bind('<Button-1>', self.freeze_branch)
        work_path_label.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)

        freeze_version_button = tk.Button(self, text="冻结所选版本", width=15)
        freeze_version_button.bind('<Button-1>', self.freeze_version)
        freeze_version_button.grid(row=6, column=1, pady=5, sticky=tk.W)

        tk.Label(
            self, text='结果:').grid(
                row=7, column=0, columnspan=2, sticky=tk.W)

        text_area = tk.Text(self, background='grey')
        text_area.grid(row=8, column=0, columnspan=3)

    # 一键创建下周分支
    def auto_create_branch(self, event):
        log_utils.clear_log_content()
        # 创建下周分支
        cmft_tools.create_next_week_branch(1174)

        logs_content = log_utils.read_logs()

        self.clear_text_area()

        self.append_text_to_text_area(logs_content)
        # 清空日志信息
        log_utils.clear_log_content()

    # 清空text_area信息
    def clear_text_area(self):
        self.text_area.delete(0.0, tk.END)

    # 向text_area追加内容
    def append_text_to_text_area(self, text_content):
        self.text_area.insert('end', text_content)
        self.text_area.mark_set('insert', 'end')

    # 冻结版本
    def freeze_version(self, event):
        print('freeze version')

    # 选择项目文件目录
    def choose_project_path(self, event):
        log_utils.clear_log_content()
        RootWindow.text_area.delete(0.0, tk.END)
        path = tk.filedialog.askdirectory()
        if path != '':
            logger.info('工作目录为:' + path)
            RootWindow.work_path_label.config(text=path)
            result, stdout, stderr = git_base.check_local_branch(path)
            logs_content = log_utils.read_logs()
            RootWindow.text_area.insert(1.0, logs_content)
        else:
            RootWindow.work_path_label.config(text="您没有选择任何目录")

    # 选择需要冻结的版本
    def freeze_branch(self, event):
        print('freeze branch')

    # set access token
    def set_access_token(self, event):
        print('set access token')

    # set projects
    def set_projects(self, event):
        print('set projects')


class AccessTokenDialog(tk.Toplevel):
    def __init__(self):
        super.__init__()
        self.title('设置Access token')
        # 弹窗界面
        self.setup_ui()

    def setup_ui(self):
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        tk.Label(row1, text='姓名：', width=8).pack(side=tk.LEFT)
        self.name = tk.StringVar()
        tk.Entry(
            row1, textvariable=self.name, width=20).pack(side=tk.LEFT)
        # 第二行
        row2 = tk.Frame(self)
        row2.pack(fill="x", ipadx=1, ipady=1)
        tk.Label(row2, text='年龄：', width=8).pack(side=tk.LEFT)
        self.age = tk.IntVar()
        tk.Entry(
            row2, textvariable=self.age, width=20).pack(side=tk.LEFT)
        # 第三行
        row3 = tk.Frame(self)
        row3.pack(fill="x")
        tk.Button(row3, text="取消").pack(side=tk.RIGHT)
        tk.Button(row3, text="确定").pack(side=tk.RIGHT)


if __name__ == '__main__':
    window = RootWindow()
    window.mainloop()
