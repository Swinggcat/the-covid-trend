from typing import List

from .. import app
from ..model.Country import Country
from ..model.Province import Province

from flask import jsonify


@app.route("/countries")
def page_countries():
    countries = Country.query.all()
    return jsonify([item.json() for item in countries])


@app.route("/country/<int:country_id>/provinces")
def page_country_provinces(country_id: int):
    country_provinces: List[Province] = Country.query.get(country_id).provinces
    return jsonify([item.json() for item in country_provinces])

