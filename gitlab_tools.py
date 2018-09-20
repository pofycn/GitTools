# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

import gitlab
import json

# private token or personal token authentication
gl = gitlab.Gitlab.from_config('cmft', ['cfg/python-gitlab.cfg'])
# gl = gitlab.Gitlab('http://git.dev.cmrh.com', private_token='1hPfJmrdmuZMuJAeS1fy')

gl.auth()


# list all the projects that yourself owned
def list_all_projects():
    projects = gl.projects.list(owned=True)
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
    project = gl.projects.get(project_id)
    return project.attributes


# Get project id and name
def get_project_name(data):
    project_name = data['name']
    project_id = data['id']
    return project_id, project_name


def test():
    print('====================test====================')
    list_all_projects()

    # list_all_groups()

    # project_info = get_project_by_id(1174)
    # project_id,project_name = get_project_name(project_info)
    # print(project_id,',',project_name)


if __name__ == '__main__':
    test()
