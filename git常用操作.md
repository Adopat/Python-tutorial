1. 初始化本地仓库

   ```
   ##选中你需要git 管理的项目使用如下命令,生成.git文件
   git init
   ```

   

2.  将文件添加到缓存区

   ```
   git add .
   ```

3. 将文件添加到本地仓库

   ```
   git commit -m '注释'
   ```

4. 关联远程库

   ```
   git remote add origin https://github.com/Adopat/Python-tutorial.git
   ```

5. 将本地库内容推送到远程

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

