#!/usr/bin/env python

import flask
import random

root = '/home/olav/Courses/bb1000/slides/classes'
app = flask.Flask(__name__, static_folder=root, static_url_path='/classes', template_folder=root)


@app.route('/')
def index():
    return flask.render_template('index.html')


port = int(5000 + 5000*random.random())
app.run(debug=True, port=port)
