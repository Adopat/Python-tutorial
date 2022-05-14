# 标准视图类
from flask import Flask
from BaseView import BaseView

app = Flask(__name__)


class UserView(BaseView):
    def get_template(self):
        return 'user.html'

    def get_date(self):
        return {
            'name': '张三',
            'gender': 'male'
        }


# UserView.as_view (‘UserView’) 创建一个名称为 UserView 的视图函数，app.add_url_rule 实际上是将 URL 路径和视图函数（由视图类的 as_view 转换而来）绑定。
app.add_url_rule('/user/', view_func=UserView.as_view('UserView'))
if __name__ == '__main__':
    app.run(debug=True)
