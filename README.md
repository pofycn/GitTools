# GitTools
给CMFT写的小小的Git封板工具
(˶‾᷄ ⁻̫ ‾᷅˵)

## 安装相关依赖
python 3.x
```
pip install arrow
```

## 功能
一键创建下周版本分支

## 操作流程
1. 选择相应工程目录
2. 点击一键创建下周分支
3. 完成

## 注意事项
此工具主要提供给项目管理员master使用，使用前请保证对应的分支有push权限，否则分支在本地创建后不能正常的Push到远端，后续会考虑增加模拟登陆来实现对分支权限的控制

## 启动
```
git clone http://git.dev.cmrh.com/chenn001/GitTools.git

cd GitTools

python client_window.py
```