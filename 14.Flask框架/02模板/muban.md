# 模板笔记

## 一、基本使用
1. 模板文件，也就是html文件，需要放到templates文件夹下，当然在`Flask(__name__,template_folder)`来修改模板的地址，但是不推荐。
2. 通过`render_template`来渲染模板。
3. 如果想要传递变量到模板中，那么可以把变量定义成字典，然后在`render_template`中，通过关键字参数的方式传递过去。`render_template('',**context)`。