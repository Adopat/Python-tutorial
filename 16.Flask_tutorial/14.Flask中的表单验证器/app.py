# Flask 中的表单验证器
from flask import Flask, render_template, request,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError

app = Flask(__name__)
# CSRF
app.config['SECRET_KEY'] = 'hard to guess string'


# def can_not_be_all_digits(form, field):
#     for char in field.data:
#         print('!', char)
#         if '0123456789'.find(char) < 0:
#             return
#     raise ValidationError('密码不能全部是数字')


class LoginForm(FlaskForm):

    # 行内验证器
    def validate_password(self, password):
        for char in password.data:
            print('!', char)
            if '0123456789'.find(char) < 0:
                return
        raise ValidationError('密码不能全部是数字')

    email = StringField(
        label='邮箱',
        validators=[
            DataRequired(message='邮箱不能为空'),
            Email(message='请输入正确的邮箱')
        ]
    )
    password = PasswordField(
        label='密码',
        validators=[
            DataRequired(message='密码不能为空'),
            Length(min=6, message='密码至少包括6个字符'),
            # can_not_be_all_digits

        ]
    )
    submit = SubmitField('登录')


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print('form.validate_on_submit() =', form.validate_on_submit())
    print('form.email.label =', form.email.label)
    print('form.email() = ', form.email)
    print('form.email.errors =', form.email.errors)
    return render_template('login.html', form=form)


@app.route('/index', methods=['post'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        dic = {}
        dic['email'] = request.form['email']
        dic['password'] = request.form['password']
        return dic
    else:
        return render_template('login.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)
