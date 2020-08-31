from .. import db


class Datum(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    province_id = db.Column(db.Integer, db.ForeignKey("provinces.id"), index=True, nullable=False)
    source_id = db.Column(db.Integer, db.ForeignKey("sources.id"), index=True, nullable=False)

    date = db.Column(db.TIMESTAMP, index=True, nullable=False)
    infected = db.Column(db.Integer, nullable=False)
    suspected = db.Column(db.Integer, nullable=False)
    cured = db.Column(db.Integer, nullable=False)
    died = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Datum#{}:Province#{}/Source#{}:{}:<INF{}:SUS{}:CUR{}:DIE{}>>'.format(
            self.id, self.province_id, self.source_id,
            self.date, self.infected, self.suspected, self.cured, self.died
        )

    def json(self):
        return {
            "id": self.id,
            "province_id": self.province_id,
            "source_id": self.source_id,

            "date": self.date,
            "infected": self.infected,
            "suspected": self.suspected,
            "cured": self.cured,
            "died": self.died,
        }