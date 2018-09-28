# GitTools
版本分支创建偷懒工具 for CMFT
(˶‾᷄ ⁻̫ ‾᷅˵)

## 安装相关依赖
python 3.x
```
pip install arrow
pip install --upgrade python-gitlab
```
## 功能
* 一键创建下周版本分支
* 查看分支功能
* 一键冻结版本

## 操作流程
1. 登录gitlab,点击个人头像选择setting

  ![](asserts/setting-1.jpg)

2. 选择Access Tokens

  ![](asserts/accesstoken-1.jpg)

3. 设置Access Token

  ![](asserts/accesstoken-2.jpg)

4. 将得到的token在窗口主界面进行设置

![image-20180928155156316](assets/image-20180928155156316.png)

5. 选择项目团队

![image-20180928155214221](assets/image-20180928155214221.png)

6. 选择项目

![image-20180928155305035](assets/image-20180928155305035.png)

7. 点击确认选择项目

![image-20180928155334494](assets/image-20180928155334494.png)

8. 点击一键创建下周分支

![image-20180928155500312](assets/image-20180928155500312.png)


9. 点击冻结所选版本：

![image-20180928155634814](assets/image-20180928155634814.png)

10. 完成

## 注意事项
此工具主要提供给项目管理员Master使用，使用时请注意生成了正确的Access Token，同时需要注意的是：能够查看到项目团队的项目信息的用户有可能因为不是Master所以会出现创建分支失败以及冻结分支失败的情况，请知悉。

## 启动
```
git clone <git repo url>>

cd GitTools

python main_window.py
```