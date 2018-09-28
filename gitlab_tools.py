# -*- coding: utf-8 -*-
"""
Gitlab API接口封装
"""

__author__ = 'Jerry Chan'

import gitlab
import json
import log_utils
import configparser

logger = log_utils.get_logger()
CONFIG_FILE = 'cfg/python-gitlab.cfg'
# private token or personal token authentication
gl = gitlab.Gitlab.from_config('cmft', [CONFIG_FILE])
# gl = gitlab.Gitlab('http://git.dev.cmrh.com', private_token='1hPfJmrdmuZMuJAeS1fy')
gl.auth()


# write access token to cfg file
def set_access_token(access_token):
    conf = configparser.ConfigParser()
    conf.read(CONFIG_FILE)
    conf.set('cmft', 'private_token', str(access_token))
    conf.write(open(CONFIG_FILE, 'w'))
    # 更新授权信息
    try:
        gl = gitlab.Gitlab.from_config('cmft', [CONFIG_FILE])
        gl.auth()
        logger.info('授权成功！')
        return gl
    except Exception as e:
        logger.info('授权失败！Exception' + str(e))


# get access token
def get_access_token():
    conf = configparser.ConfigParser()
    conf.read(CONFIG_FILE)
    access_token = conf.get('cmft', 'private_token')
    return access_token


# list all the projects that you can see
def list_all_projects():
    projects = gl.projects.list(
        order_by='name', sort='asc', visibility='private')
    # for project in projects:
    #     logger.info('project detail--->project id:' +
    #                 str(project.attributes['id']) + ',' + 'project-name:' +
    #                 str(project.attributes['name']))
    logger.info('获取项目列表成功！')
    # logger.info(projects)
    return projects


# list all the groups
def list_all_groups():
    all_groups = gl.groups.list()
    # for group in all_groups:
    #     logger.info('group detail--->group id:' + str(group.attributes['id']) +
    #                 ',' + 'group-name:' + group.attributes['name'] + ',' +
    #                 'description:' + group.attributes['description'])
    # logger.info('group info:' + str(group))
    return all_groups


# list projects in the group
def list_projects_in_group(group_id):
    group = gl.groups.get(group_id)
    projects = group.projects.list()
    # for project in projects:
    #     logger.info('project detail--->project id:' +
    #                 str(project.attributes['id']) + ',' + 'project-name:' +
    #                 str(project.attributes['name']))
    logger.info('获取项目列表成功！')
    return projects


# Get a project by ID
def get_project_by_id(project_id):
    try:
        project = gl.projects.get(project_id)
        # print('获取项目信息成功!',project)
        logger.info('获取项目信息成功! 项目名:' + project.attributes['name'])
        return project
    except Exception as e:
        logger.info('获取项目信息失败!' + e)


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
        logger.info('获取分支信息成功！结果:' + str(branch_name_list))
        return branch_name_list
    except Exception as e:
        logger.info('获取分支信息失败！' + e)
        return


# protect branch by branch name
def protect_branch(project_id, branch_name):
    try:
        project = get_project_by_id(project_id)
        branch = project.branches.get(branch_name)
        branch.protect(allowed_to_push='no one', allowed_to_merge='no one')
        logger.info('关闭分支developoer提交、合并权限成功，分支名:' + branch_name)
    except Exception as e:
        logger.info('关闭分支developoer提交、合并权限失败' + branch_name)
        return


# unprotect branch by branch name
def unprotect_branch(project_id, branch_name):
    try:
        project = get_project_by_id(project_id)
        branch = project.branches.get(branch_name)
        branch.unprotect()
        logger.info('开放分支提交、合并权限成功，分支名:' + branch_name)
    except Exception as e:
        logger.info('开放分支提交、合并权限失败！' + e)
        return


# create branch
def create_branch(project_id, branch_name, ref_branch):
    try:
        project = get_project_by_id(project_id)
        branch = project.branches.create({
            'branch': branch_name,
            'ref': ref_branch
        })
        logger.info('以' + ref_branch + '创建分支:' + branch_name + '---成功！')
        return branch
    except Exception as e:
        logger.info('创建分支失败！' + e)
        return


# delete branch
def delete_branch(project_id, branch_name):
    try:
        project = get_project_by_id(project_id)
        branch = project.branches.delete(branch_name)
        logger.info('删除分支:' + branch_name + '---成功！')
    except Exception as e:
        logger.info('删除分支失败！' + e)
        return


def test():
    print('====================test====================')
    # list_all_projects()

    # list_all_groups()
    # list_projects_in_group(717)

    # branches = get_branches_names_by_project_id(51)
    # print(branches)

    # project_info = get_project_by_id(1174)
    # project_id,project_name = get_project_name(project_info)
    # print(project_id,',',project_name)

    # protect_branch(51, 'dev_20181018')
    # unprotect_branch(1174, 'release')

    # branch = create_branch(1174, 'dev_20180920')
    # delete_branch(1174, 'dev_20180927')
    # delete_branch(1174, 'release_20180927')


if __name__ == '__main__':
    test()
