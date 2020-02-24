#!flask/bin/python
from flask import Flask
from flaskrun import flaskrun
from flask import render_template
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

# @application.route('/hello/')
# @application.route('hello/<name>)
@application.route('/', methods=['GET'])
def hello():
    return 'Flask and React Finally Integrated!'
    # return render_template('hello.html', name=name)

@application.route('/', methods=['POST'])
def post():
    return '{"Output":"Hello World"}'

if __name__ == '__main__':
    flaskrun(application)
