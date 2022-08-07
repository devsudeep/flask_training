# Flask Getting Started

## python 2
```sh

$ pip install virtualenv
$ pip install virtualenv
$ virtualenv env
$ virtualenv --version

# install pip-autoremove
pip install pip-autoremove
# remove "somepackage" plus its dependencies:
pip-autoremove somepackage -y
or 

python3 -m venv virtual-environment-name
$ source env/bin/activate

pip install flask
```

## python 3
```sh
python3 -m venv virtual-environment-name
$ source env/bin/activate
. flask_training/bin/activate  # mac
pip install flask
```
Flask has three main dependencies. The routing, debugging, and Web Server Gateway Interface (WSGI) subsystems come from Werkzeug; the template support is provided by Jinja2; and the command-line integration comes from Click. These dependencies are all authored by Armin Ronacher, the author of Flask.

Verify install

```sh
>> python
import flask
```
# Chapter 2. Basic Application Structure
## Initialization

All Flask applications must create an application instance. The web server passes all requests it receives from clients to this object for handling, using a protocol called Web Server Gateway Interface (WSGI, pronounced “wiz-ghee”). The application instance is an object of class Flask

Flask uses this argument to determine the location of the application, which in turn allows it to locate other files that are part of the application, such as images and templates.

## Routes and View Functions
```python
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
```
 1. registers function index() as the handler
 2. app.route decorator is the preferred method to register view functions
 3. app.add_url_rule() method, which in its most basic form takes three arguments: the URL
 4. Functions like index() that handle application URLs are called view functions. 
 
The portion of the route URL enclosed in angle brackets is the dynamic part. Any URLs that match the static portions will be mapped to this route, and when the view function is invoked, the dynamic component will be passed as an argument. In the preceding example, the name argument is used to generate a response that includes a personalized greeting.

Flask supports the 
types 
string 
int
float
path for routes. 

The **path** type is a special string type that can include forward slashes, unlike the string type.

## Development Web Server
Flask applications include a development web server that can be started with the flask run command. This command looks for the name of the Python script that contains the application instance in the FLASK_APP environment variable.
```sh
export FLASK_APP=hello.py
flask run
```

```error 
Error: Importerror: cannot import name ‘escape’ from ‘jinja2’ ( Solved )

Solution:
    pip install Jinja2==3.0.3

```