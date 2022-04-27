from flask import Flask
from apps.book import bp as book_bp
from apps.course import bp as course_bp
from apps.user import bp as user_bp

app = Flask(__name__)
app.register_blueprint(book_bp)
app.register_blueprint(course_bp)
app.register_blueprint(user_bp)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
