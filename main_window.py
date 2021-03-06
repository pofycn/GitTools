# -*- coding: utf-8 -*-
"""
窗口程序，程序主入口
"""

__author__ = 'Jerry Chan'

import tkinter as tk
import arrow
import gitlab_tools
import log_utils
import version_tools_cmft as cmft_tools

logger = log_utils.get_logger()
DEFAULT_ACCESS_TOKEN = '请点击设置access token'
DEFAILT_PROJECT_NAME = '请点击选择项目进行管理'
DEFAILT_GROUP_NAME = '请点击选择项目团队'


# main window
class RootWindow(tk.Tk):
    def __init__(self):
        # 创建窗口程序
        super().__init__()
        self.title('CMFT Git Tools')
        self.resizable(False, False)
        # 重置日志信息
        log_utils.clear_log_content()

        self.access_token_label = tk.Label(
            self, text=DEFAULT_ACCESS_TOKEN, relief=tk.GROOVE, width=30)
        self.choose_project_label = tk.Label(
            self, text=DEFAILT_PROJECT_NAME, relief=tk.GROOVE, width=30)
        self.choose_group_label = tk.Label(
            self, text=DEFAILT_GROUP_NAME, relief=tk.GROOVE, width=30)

        access_token = gitlab_tools.get_access_token()
        if access_token != None and access_token != '':
            gitlab_tools.set_access_token(access_token)
            self.access_token_label.config(text=access_token)
        else:
            logger.info('授权失败，请重新设置access token')
            self.access_token_label.config(text='授权失败，请重新设置access token')
        # 初始化程序界面
        self.setup_ui()
        self.display_log_content_on_terminal()

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

        # access_token_label = tk.Label(
        #     self, text='请点击设置access token', relief=tk.GROOVE, width=30)
        self.access_token_label.bind('<Button-1>', self.setup_accesstoken)
        self.access_token_label.grid(
            row=2, column=1, padx=5, pady=5, sticky=tk.W)

        tk.Label(
            self, text='项目团队:').grid(
                row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.choose_group_label.bind('<Button-1>', self.setup_group)
        self.choose_group_label.grid(
            row=3, column=1, padx=5, pady=5, sticky=tk.W)

        tk.Label(
            self, text='项目名：').grid(
                row=4, column=0, padx=5, pady=5, sticky=tk.W)
        # choose_project_label = tk.Label(
        #     self, text='请点击选择项目进行管理', relief=tk.GROOVE, width=30)
        self.choose_project_label.bind('<Button-1>', self.setup_projects)
        self.choose_project_label.grid(
            row=4, column=1, padx=5, pady=5, sticky=tk.W)

        create_next_branch_button = tk.Button(self, text="一键创建下周版本", width=15)
        create_next_branch_button.bind('<Button-1>', self.auto_create_branch)
        create_next_branch_button.grid(row=5, column=1, pady=5, sticky=tk.W)

        tk.Label(
            self, text='版本冻结:').grid(
                row=6, column=0, padx=5, pady=5, sticky=tk.W)

        self.branch_label = tk.Label(
            self, text='请点击选择需要冻结的版本', relief=tk.GROOVE, width=30)
        self.branch_label.bind('<Button-1>', self.setup_freeze_branch)
        self.branch_label.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)

        freeze_version_button = tk.Button(self, text="冻结所选版本", width=15)
        freeze_version_button.bind('<Button-1>', self.freeze_version)
        freeze_version_button.grid(row=7, column=1, pady=5, sticky=tk.W)

        tk.Label(
            self, text='结果:').grid(
                row=8, column=0, columnspan=2, sticky=tk.W)

        self.text_area = tk.Text(self, background='grey')
        self.text_area.grid(row=9, column=0, columnspan=3)

    # 一键创建下周分支
    def auto_create_branch(self, event):
        # 获取选择的项目id
        project_info = str(self.choose_project_label.cget('text'))
        project_id = project_info.split(':')[0]

        # 创建下周分支
        cmft_tools.create_next_week_branch(project_id)
        self.display_log_content_on_terminal()

    # 在text area显示日志信息
    def display_log_content_on_terminal(self):
        logs_content = log_utils.read_logs()
        self.clear_text_area()
        self.append_text_to_text_area(logs_content)

    # 清空text_area信息
    def clear_text_area(self):
        self.text_area.delete(0.0, tk.END)

    # 向text_area追加内容
    def append_text_to_text_area(self, text_content):
        self.text_area.insert('end', text_content)
        self.text_area.mark_set('insert', 'end')

    # 设置冻结分支
    def setup_freeze_branch(self, event):
        branch_name = self.list_branch_name(self)
        self.branch_label.config(text=branch_name)

    # 选择需要冻结的版本
    def list_branch_name(self, event):
        branch_list_dialog = branchListDialog(self)
        self.wait_window(branch_list_dialog)
        self.display_log_content_on_terminal()
        return branch_list_dialog.branch_name

    # 执行冻结版本操作
    def freeze_version(self, event):
        project_info = str(self.choose_project_label.cget('text')).split(':')
        project_id = project_info[0]
        project_name = project_info[1]
        branch_name = str(self.branch_label.cget('text'))
        logger.info('准备冻结' + project_name + '项目的' + branch_name + '分支')
        gitlab_tools.protect_branch(project_id, branch_name)
        self.display_log_content_on_terminal()

    # set access token
    def set_access_token(self, event):
        access_token_dialog = AccessTokenDialog()
        self.wait_window(access_token_dialog)
        self.display_log_content_on_terminal()
        return access_token_dialog.accesstoken

    # set access token to label
    def setup_accesstoken(self, event):
        access_token = self.set_access_token(self)
        if access_token is None:
            logger.info('授权失败！')
            return
        logger.info('授权成功！')
        self.access_token_label.config(text=access_token)
        gitlab_tools.set_access_token(access_token)
        self.display_log_content_on_terminal()

    # set group
    def set_group(self, event):
        group_dialog = GroupsDialog(self)
        self.wait_window(group_dialog)
        self.display_log_content_on_terminal()
        return group_dialog.group_name

    def setup_group(self, event):
        group_name = self.set_group(self)
        if group_name is None:
            return
        self.choose_group_label.config(text=group_name)
        self.display_log_content_on_terminal()

    # set projects
    def set_projects(self, event):
        project_name_dialog = ProjectsDialog(self)
        self.wait_window(project_name_dialog)
        self.display_log_content_on_terminal()
        return project_name_dialog.project_name

    def setup_projects(self, event):
        project_name = self.set_projects(self)
        if project_name is None:
            return
        self.choose_project_label.config(text=project_name)
        self.display_log_content_on_terminal()


class AccessTokenDialog(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('设置Access token')
        # 弹窗界面
        self.setup_ui()

    def setup_ui(self):
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        tk.Label(row1, text='access token：', width=15).pack(side=tk.LEFT)
        self.accesstoken = tk.StringVar()
        tk.Entry(
            row1, textvariable=self.accesstoken, width=30).pack(side=tk.RIGHT)

        row2 = tk.Frame(self)
        row2.pack(fill="x")
        tk.Button(row2, text="取消", command=self.cancel).pack(side=tk.RIGHT)
        tk.Button(row2, text="确定", command=self.ok).pack(side=tk.RIGHT)

    def ok(self):
        self.accesstoken = self.accesstoken.get()
        self.destroy()

    def cancel(self):
        self.accesstoken = None
        self.destroy()


class GroupsDialog(tk.Toplevel):
    def __init__(self, root_window):
        super().__init__()
        self.title('选择项目团队')
        self.root_window = root_window
        # 弹窗界面
        self.setup_ui()

    def setup_ui(self):
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        # 加载项目列表
        groups = gitlab_tools.list_all_groups()

        tk.Label(row1, text='项目团队信息').pack(side=tk.TOP)
        self.group_name = tk.StringVar()

        row2 = tk.Frame(self)
        row2.pack(fill="y")
        for group in groups:
            label_display_value = str(group.attributes['id']) + ':' + str(
                group.attributes['name'])
            radio_button_display_name = group.attributes[
                'name'] + ' ' + group.attributes['description']
            tk.Radiobutton(
                row2,
                variable=self.group_name,
                text=radio_button_display_name,
                value=str(label_display_value),
                padx=10,
                pady=5).pack(anchor=tk.W)

        self.group_name.set(
            str(groups[0].attributes['id']) + ':' +
            str(groups[0].attributes['name']))
        row3 = tk.Frame(self)
        row3.pack(fill="x")
        tk.Button(row3, text="取消", command=self.cancel).pack(side=tk.RIGHT)
        tk.Button(row3, text="确定", command=self.ok).pack(side=tk.RIGHT)

    def ok(self):
        self.group_name = self.group_name.get()
        self.destroy()

    def cancel(self):
        self.group_name = None
        self.destroy()


class ProjectsDialog(tk.Toplevel):
    def __init__(self, root_window):
        super().__init__()
        self.title('选择项目')
        self.root_window = root_window
        # 弹窗界面
        self.setup_ui()

    def setup_ui(self):
        row1 = tk.Frame(self)
        row1.pack(fill="x")

        group_info = str(self.root_window.choose_group_label.cget('text'))
        group_id = group_info.split(':')[0]

        # 加载项目列表
        projects = gitlab_tools.list_projects_in_group(group_id)

        tk.Label(row1, text='项目名称').pack(side=tk.TOP)
        self.project_name = tk.StringVar()

        row2 = tk.Frame(self)
        row2.pack(fill="y")
        for project in projects:
            label_display_value = str(project.attributes['id']) + ':' + str(
                project.attributes['name'])
            tk.Radiobutton(
                row2,
                variable=self.project_name,
                text=str(project.attributes['name']),
                value=str(label_display_value),
                padx=10,
                pady=5).pack(anchor=tk.W)

        self.project_name.set(
            str(projects[0].attributes['id']) + ':' +
            str(projects[0].attributes['name']))
        row3 = tk.Frame(self)
        row3.pack(fill="x")
        tk.Button(row3, text="取消", command=self.cancel).pack(side=tk.RIGHT)
        tk.Button(row3, text="确定", command=self.ok).pack(side=tk.RIGHT)

    def ok(self):
        self.project_name = self.project_name.get()
        self.destroy()

    def cancel(self):
        self.project_name = None
        self.destroy()


class branchListDialog(tk.Toplevel):
    def __init__(self, root_window):
        super().__init__()
        self.title('选择分支')
        self.root_window = root_window
        # 弹窗界面
        self.setup_ui()

    def setup_ui(self):
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        project_info = str(self.root_window.choose_project_label.cget('text'))
        project_id = project_info.split(':')[0]
        # 确认project id是否为空
        if (project_id == None and project_id == DEFAILT_PROJECT_NAME):
            logger.info('项目名错误！' + project_id)
            return
        # 加载项目所有分支
        branch_name_list = gitlab_tools.get_branches_names_by_project_id(
            project_id)

        tk.Label(row1, text='分支名称').pack(side=tk.TOP)
        self.branch_name = tk.StringVar()

        row2 = tk.Frame(self)
        row2.pack(fill="y")
        for branch_name in branch_name_list:
            tk.Radiobutton(
                row2,
                variable=self.branch_name,
                text=str(branch_name),
                value=str(branch_name),
                padx=10,
                pady=5).pack(anchor=tk.W)

        self.branch_name.set(str(branch_name_list[0]))
        row3 = tk.Frame(self)
        row3.pack(fill="x")
        tk.Button(row3, text="取消", command=self.cancel).pack(side=tk.RIGHT)
        tk.Button(row3, text="确定", command=self.ok).pack(side=tk.RIGHT)

    def ok(self):
        self.branch_name = self.branch_name.get()
        self.destroy()

    def cancel(self):
        self.branch_name = None
        self.destroy()


if __name__ == '__main__':
    window = RootWindow()
    window.mainloop()
