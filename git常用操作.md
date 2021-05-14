1. 下载 git 安装

   ```
   # 1. 设置用户名
   git config --global user.name "Your GitHub Name"
   # 2. 设置邮箱
   git config --global user.email "注册GitHub邮箱"
   # 3. 查看当前登录邮箱
   git config user.name
   # 4. 查看当前登录账号
   git config user.name
   # 5. 修改用户名
   git config --global user.name "Your Name"
   # 6. 修改邮箱
   git config --global user.email "Your email"
   ```

   

2. 初始化本地仓库

   ```
   ##选中你需要git 管理的项目使用如下命令,生成.git文件
   git init
   ```

   

3. 生成 ssh 用于 GitHub验证

   ```
   在命令框中输入 $ ssh-keygen -t rsa -C "email@example.com" 按三次回车生成公钥，在C:\Users\Administrator.ssh下找到id_rsa.pub文件，记事本打开复制公钥。
   当然这里也是有提示的。
   然后在 github 中设置SSH 
   将Key添加到ssh-agent
   ssh-add ~/.ssh/id_rsa
   验证是都配置成功：
   ssh - T git@github.com
   ```

   > ssh-keygen -C "email@example.mail" -t rsa linux 命令

4. 将文件添加到缓存区

   ```
   git add .
   ```

5. 将文件添加到本地仓库

   ```
   git commit -m '注释'
   ```

6. 关联远程库

   ```
   git remote add origin https://github.com/Adopat/Python-tutorial.git
   ```

7. 将本地库内容推送到远程

   ```
   git push -u origin master
   ```

> 注意 将本地库内容推送到远程时可能会提示输入用户名密码使用以下方式解决，改用SSH提交

```
git remote rm origin
git remote add origin SSH  （注意此ssh是你的ssh地址）
git push -u origin master
```

总结

```
git init //初始化仓库
git add . // 添加问价到暂存区
git commit -m 'first commit' // 提交文件到本地仓库
git remote add origin https://github.com/Adopat/Python-tutorial.git
git pull origin master  //把本地仓库的变化连接到远程仓库master分支，用于同步
git push -u origin master  //把本地仓库的文件推送到远程仓库master 分支
```
pip freeze>requirements.txt  -- 生成requirements.txt 文件
pip install -r requirements.txt -- 安装 requirements.txt 文件中的安装包
