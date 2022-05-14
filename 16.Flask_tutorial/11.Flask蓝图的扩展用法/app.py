from flask import Flask
import news
import products

app = Flask(__name__)
# 视图注册
app.register_blueprint(news.blueprint)
app.register_blueprint(products.blueprint)
if __name__ == '__main__':
    app.run(debug=True)
