from .. import app

from flask import send_from_directory


@app.route("/")
def page_index():
    return send_from_directory('static', 'index.html')