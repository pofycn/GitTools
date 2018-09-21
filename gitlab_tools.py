# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

import gitlab
import json

# private token or personal token authentication
gl = gitlab.Gitlab.from_config('cmft', ['cfg/python-gitlab.cfg'])
# gl = gitlab.Gitlab('http://git.dev.cmrh.com', private_token='1hPfJmrdmuZMuJAeS1fy')

gl.auth()


# list all the projects that you can see
def list_all_projects():
    projects = gl.projects.list(all=True, order_by='name', sort='asc')
    for project in projects:
        print('project detail--->project id:', project.attributes['id'], ',',
              'project-name:', project.attributes['name'])
    return projects


# list all the groups
def list_all_groups():
    all_groups = gl.groups.list()
    for group in all_groups:
        print('group detail--->group id:', group.attributes['id'], ',',
              'group-name:', group.attributes['name'])
    return all_groups


# Get a project by ID
def get_project_by_id(project_id):
    try:
        project = gl.projects.get(project_id)
        # print('获取项目信息成功!',project)
        print('获取项目信息成功! 项目名:', project.attributes['name'])
        return project
    except Exception as e:
        print('获取项目信息失败!', e)


# Get project id and name
def get_project_name(data):
    project_name = data['name']
    project_id = data['id']
    return project_id, project_name


# get branches info by project id
def get_branches_names_by_project_id(project_id):
    try:
        branches = get_project_by_id(project_id).branches.list()
        branch_name_list = []
        for branch in branches:
            branch_name_list.append(branch.attributes['name'])
        print('获取分支信息成功！结果:', branch_name_list)
        return branch_name_list
    except Exception as e:
        print('获取分支信息失败！', e)
        return


# protect branch by branch name
def protect_branch(project_id, branch_name):
    try:
        project = get_project_by_id(project_id)
        branch = project.branches.get(branch_name)
        branch.protect(allowed_to_push='no one', allowed_to_merge='no one')
        print('关闭分支developoer提交、合并权限成功，分支名:', branch_name)
    except Exception as e:
        print('关闭分支developoer提交、合并权限失败', branch_name)
        return


# unprotect branch by branch name
def unprotect_branch(project_id, branch_name):
    try:
        project = get_project_by_id(project_id)
        branch = project.branches.get(branch_name)
        branch.unprotect()
        print('开放分支提交、合并权限成功，分支名:', branch_name)
    except Exception as e:
        print('开放分支提交、合并权限失败！', e)
        return


# create branch
def create_branch(project_id, branch_name, ref_branch):
    try:
        project = get_project_by_id(project_id)
        branch = project.branches.create({
            'branch': branch_name,
            'ref': ref_branch
        })
        print('以', ref_branch, '创建分支:', branch_name, '---成功！')
        return branch
    except Exception as e:
        print('创建分支失败！', e)
        return


# delete branch
def delete_branch(project_id, branch_name):
    try:
        project = get_project_by_id(project_id)
        branch = project.branches.delete(branch_name)
        print('删除分支:', branch_name, '---成功！')
    except Exception as e:
        print('删除分支失败！', e)
        return


def test():
    print('====================test====================')
    # list_all_projects()

    # list_all_groups()

    # branches = get_branches_names_by_project_id(1174)

    # project_info = get_project_by_id(1174)
    # project_id,project_name = get_project_name(project_info)
    # print(project_id,',',project_name)

    # protect_branch(1174, 'release')
    # unprotect_branch(1174, 'release')

    # branch = create_branch(1174, 'dev_20180920')
    # delete_branch(1174, 'dev')
    # delete_branch(1174, 'release')


if __name__ == '__main__':
    test()
