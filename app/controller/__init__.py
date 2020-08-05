from .. import app
from flask import render_template


@app.route('/')
def page_index():
    return render_template('index.jinja2')

