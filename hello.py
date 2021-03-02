from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # return "<h1>Hello World</h1>"\
    return render_template("index.html")


@app.route('/user/<name>')
def user(name):
    # return "<h1>Hello {}</h1>".format(name)
    return render_template("user.html", user_name=name)


# Ivalid URL

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal server error


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
