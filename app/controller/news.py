from .. import app, db
from ..model.News import News

from flask import jsonify

from datetime import datetime


@app.route("/api/news/today")
def page_news_today():
    news = News.query \
        .filter(News.date >= datetime.now().date()) \
        .order_by(News.date.desc()) \
        .all()
    return jsonify([item.json() for item in news])


@app.route("/api/news/all")
def page_news_all():
    news = News.query\
        .order_by(News.date.desc())\
        .limit(50)\
        .all()
    return jsonify([item.json() for item in news])

