from .. import db


class Province(db.Model):
    __tablename__ = "provinces"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey("countries.id"), index=True, nullable=False)
    name = db.Column(db.VARCHAR(32), nullable=False, index=True)

    data = db.relationship("Datum", backref="province")

    def __repr__(self):
        return '<Province#{}:"{}" of Country#{}>'.format(self.id, self.name, self.country_id)
