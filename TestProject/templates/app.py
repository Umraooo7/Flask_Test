from ensurepip import bootstrap
import imp
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<h1>Hello, Abhish!</h1>"

@app.route("/about/<username>")
def about_page(username):
    return f'<h1> Hi {escape(username)}, This is About Page </h1>'

@app.route("/")
@app.route('/home')
@app.route('/Home')
@app.route('/HOME')
def home_page():
    return render_template('hello.html')

# using jinja editing in Helloworld.html, render_template()
@app.route("/helloworld/<name>")
def helloWorld(name):
    return render_template('HelloWorld.html',name=name)

@app.route('/post/<int:post_id1>,<int:post_id2>')
def show_post(post_id1,post_id2):
    return f'<h2>First No.- {post_id1}, Second No.- {post_id2}</h2><br>Total: {post_id2 + post_id1}'

@app.route('/path/<path:subpath>')
def show_path(subpath):
    return f'<b>The subpath is {subpath}</b>'

# page not found, can add the page at error 404, using render_template
@app.errorhandler(404)
def page_not_found(error):
    return f"Sorry, wrong url"
# render_template('page_not_found.html'), 404
