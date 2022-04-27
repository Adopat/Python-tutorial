from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/control")
def control():
    context = {
        "age": 17,
        'books': ['红楼梦', '三国演义', '水浒传', '西游记'],
        "person": {"name": "zhiliao", "age": 18}
    }
    return render_template("control.html", **context)
    # return jsonify(context)


@app.route("/about")
def about():
    context = {
        "username": "周杰伦",
        'books': ['红楼梦', '三国演义']
    }
    return render_template("about.html", **context)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/test_obj')
def test_obj():
    user = {
        'username': 'Justin',
        'age': '18'
    }
    return render_template('test_obj.html', user=user)


if __name__ == '__main__':
    app.run()
