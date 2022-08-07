from flask import Flask

print(__name__)

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello world</h1'


app.add_url_rule('/', 'index', index)


@app.route('/user/<name>')
def user(name):
    return '<h1>User {}</h1>'.format(name)


app.run()
