from typing import List

from .. import app, db
from ..model.Country import Country
from ..model.Province import Province
from ..model.Datum import Datum

from flask import jsonify


@app.route("/api/countries")
def page_countries():
    countries = Country.query.all()
    return jsonify([item.json() for item in countries])


@app.route("/api/country/<int:country_id>/provinces")
def page_country_provinces(country_id: int):
    country_provinces: List[Province] = Country.query.get(country_id).provinces
    return jsonify([item.json() for item in country_provinces])


@app.route("/api/province/<int:province_id>/latest")
def page_province_data_latest(province_id: int):
    latest_data: Datum or None = Datum.query\
        .filter(Datum.province_id == province_id)\
        .order_by(Datum.date.desc()) \
        .limit(1) \
        .one_or_none()
    if latest_data is None:
        return None
    return latest_data.json()


@app.route("/api/data/countries")
def page_data_countries():
    return jsonify([{
        "country_name": i.country_name,
        "suspected": i.total_suspected,
        "cured": i.total_cured,
        "died": i.total_died,
        "infected": i.total_infected
    } for i in db.session.execute("select * from latest_country_data")])


@app.route("/api/data/provinces")
def page_data_provinces():
    return jsonify([{
        "country_name": i.country_name,
        "suspected": i.total_suspected,
        "cured": i.total_cured,
        "died": i.total_died,
        "infected": i.total_infected
    } for i in db.session.execute("select * from latest_country_data")])